#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import os
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GAME_DEFS = {
    "dow2": {
        "name": "Dawn of War 2",
        "root": Path("Dawn of War 2"),
    },
    "retribution": {
        "name": "Dawn of War II - Retribution",
        "root": Path("Dawn of War II - Retribution"),
    },
}

ID_LINE = re.compile(r"^(\d+)\t(.*)$")
ASCII_WORD = re.compile(r"[A-Za-z]{3,}")

FINAL_REPLACEMENTS = (
    ("帝國衛隊士兵", "星界軍士兵"),
    ("帝國衛隊老兵", "星界軍老兵"),
    ("帝國衛隊防衛部隊", "星界軍防衛部隊"),
    ("帝國衛隊", "星界軍"),
    ("帝國防衛軍", "星界軍"),
    ("帝國衛兵", "星界軍士兵"),
)


def resolve_path(value: str | Path) -> Path:
    return Path(value).expanduser().resolve()


def project_root(args: argparse.Namespace) -> Path:
    if args.project_root:
        return resolve_path(args.project_root)
    return resolve_path(args.process_root) / "translation_project"


def glossary_path(args: argparse.Namespace) -> Path:
    if args.glossary:
        return resolve_path(args.glossary)
    return ROOT / "glossary" / "mainland_40k_tw.tsv"


def overrides_path(args: argparse.Namespace) -> Path:
    if args.overrides:
        return resolve_path(args.overrides)
    return project_root(args) / "work" / "manual_overrides.tsv"


def games(args: argparse.Namespace) -> dict[str, dict[str, Path | str]]:
    process_root = resolve_path(args.process_root)
    result: dict[str, dict[str, Path | str]] = {}
    for key, meta in GAME_DEFS.items():
        game_root = process_root / meta["root"]
        result[key] = {
            "name": meta["name"],
            "en": game_root / "Locale" / "English" / "DOW2.ucs",
            "zh": game_root / "Locale" / "TChinese" / "DOW2.ucs",
        }
    return result


def read_ucs(path: Path) -> OrderedDict[str, str]:
    entries: OrderedDict[str, str] = OrderedDict()
    with path.open("r", encoding="utf-16") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.rstrip("\r\n")
            if not line:
                continue
            match = ID_LINE.match(line)
            if not match:
                continue
            entries[match.group(1)] = match.group(2)
    return entries


def write_ucs(path: Path, entries: OrderedDict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-16", newline="\r\n") as handle:
        for key, value in entries.items():
            handle.write(f"{key}\t{value}\n")


def read_glossary(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def apply_avoid_replacements(text: str, glossary: list[dict[str, str]]) -> str:
    result = text
    for row in glossary:
        preferred = row.get("preferred_tw", "").strip()
        avoid = row.get("avoid_tw", "").strip()
        if not preferred or not avoid:
            continue
        avoid_terms = sorted(
            [item.strip() for item in avoid.split(";") if item.strip()],
            key=len,
            reverse=True,
        )
        for bad in avoid_terms:
            # Avoid automatic substring expansion such as 泰倫蟲族 -> 泰倫蟲族蟲族.
            # These still appear in term-report for human review.
            if bad == preferred or bad in preferred:
                continue
            result = result.replace(bad, preferred)
    return result


def apply_final_replacements(text: str) -> str:
    result = text
    for old, new in FINAL_REPLACEMENTS:
        result = result.replace(old, new)
    return result


def classify(en_text: str, zh_text: str | None) -> str:
    if zh_text is None:
        return "missing_in_tchinese"
    if zh_text == en_text:
        return "same_as_english"
    if ASCII_WORD.search(zh_text):
        return "contains_ascii"
    return "has_tchinese"


def cmd_report(args: argparse.Namespace) -> None:
    rows = []
    for key, meta in games(args).items():
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        missing = [item for item in en if item not in zh]
        extra = [item for item in zh if item not in en]
        same = [item for item in en if item in zh and en[item] == zh[item]]
        ascii_rows = [item for item in en if item in zh and ASCII_WORD.search(zh[item])]
        rows.append({
            "game_key": key,
            "game": meta["name"],
            "english_ids": len(en),
            "tchinese_ids": len(zh),
            "missing_in_tchinese": len(missing),
            "extra_in_tchinese": len(extra),
            "same_as_english": len(same),
            "contains_ascii": len(ascii_rows),
            "first_missing_ids": ", ".join(missing[:20]),
        })

    out = project_root(args) / "reports" / "coverage.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(out)


def cmd_export(args: argparse.Namespace) -> None:
    glossary = read_glossary(glossary_path(args))
    all_games = games(args)
    targets = all_games.keys() if args.game == "all" else [args.game]
    for key in targets:
        meta = all_games[key]
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        out = project_root(args) / "work" / f"{key}_translation.tsv"
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8-sig", newline="") as handle:
            fields = ["id", "status", "en", "zh_current", "zh_new", "notes"]
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            for text_id, en_text in en.items():
                zh_current = zh.get(text_id, "")
                zh_suggested = apply_avoid_replacements(zh_current, glossary) if zh_current else ""
                writer.writerow({
                    "id": text_id,
                    "status": classify(en_text, zh_current if text_id in zh else None),
                    "en": en_text,
                    "zh_current": zh_current,
                    "zh_new": zh_suggested if zh_suggested != zh_current else "",
                    "notes": "",
                })
        print(out)


def cmd_build(args: argparse.Namespace) -> None:
    all_games = games(args)
    targets = all_games.keys() if args.game == "all" else [args.game]
    manual_overrides: dict[tuple[str, str], str] = {}
    manual_by_source: dict[str, str] = {}
    manual_path = overrides_path(args)
    if manual_path.exists():
        with manual_path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                value = row.get("zh_new", "")
                if value:
                    game_key = row.get("game_key", "")
                    text_id = row.get("id", "")
                    source = row.get("en", "")
                    if game_key and text_id:
                        manual_overrides[(game_key, text_id)] = value
                    if source:
                        manual_by_source[source] = value

    for key in targets:
        meta = all_games[key]
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        work = project_root(args) / "work" / f"{key}_translation.tsv"
        overrides: dict[str, str] = {}
        if work.exists():
            with work.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle, delimiter="\t"):
                    value = row.get("zh_new", "")
                    if value:
                        overrides[row["id"]] = value

        output = OrderedDict()
        for text_id, en_text in en.items():
            if (key, text_id) in manual_overrides:
                output[text_id] = manual_overrides[(key, text_id)]
            elif ("all", text_id) in manual_overrides:
                output[text_id] = manual_overrides[("all", text_id)]
            elif en_text in manual_by_source:
                output[text_id] = manual_by_source[en_text]
            elif text_id in overrides:
                output[text_id] = overrides[text_id]
            elif text_id in zh:
                output[text_id] = zh[text_id]
            elif args.fill_missing == "english":
                output[text_id] = en_text
            else:
                output[text_id] = ""

            output[text_id] = apply_final_replacements(output[text_id])

        out = project_root(args) / "output" / key / "Locale" / "TChinese" / "DOW2.ucs"
        write_ucs(out, output)
        print(out)


def cmd_term_report(args: argparse.Namespace) -> None:
    glossary = read_glossary(glossary_path(args))
    rows = []
    for key, meta in games(args).items():
        zh = read_ucs(meta["zh"])
        for text_id, text in zh.items():
            for term in glossary:
                preferred = term.get("preferred_tw", "").strip()
                avoid = term.get("avoid_tw", "").strip()
                if not avoid:
                    continue
                for bad in [item.strip() for item in avoid.split(";") if item.strip()]:
                    if bad and bad != preferred and bad in text:
                        rows.append({
                            "game_key": key,
                            "id": text_id,
                            "avoid_tw": bad,
                            "preferred_tw": preferred,
                            "text": text,
                        })

    out = project_root(args) / "reports" / "term_risks.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8-sig", newline="") as handle:
        fields = ["game_key", "id", "avoid_tw", "preferred_tw", "text"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Dawn of War II UCS translation pipeline")
    default_process_root = os.environ.get("DOW2_PROCESS_ROOT", str(ROOT.parent))
    parser.add_argument(
        "--process-root",
        default=default_process_root,
        help="Local folder that contains the copied game folders, for example I:\\translate_process.",
    )
    parser.add_argument(
        "--project-root",
        default=None,
        help="Local folder for reports/work/output. Defaults to <process-root>\\translation_project.",
    )
    parser.add_argument(
        "--glossary",
        default=None,
        help="Optional glossary TSV path. Defaults to glossary/mainland_40k_tw.tsv in this repository.",
    )
    parser.add_argument(
        "--overrides",
        default=None,
        help="Optional manual overrides TSV. Defaults to <project-root>\\work\\manual_overrides.tsv.",
    )
    sub = parser.add_subparsers(required=True)

    report = sub.add_parser("report")
    report.set_defaults(func=cmd_report)

    export = sub.add_parser("export")
    export.add_argument("--game", choices=["all", *GAME_DEFS.keys()], default="all")
    export.set_defaults(func=cmd_export)

    build = sub.add_parser("build")
    build.add_argument("--game", choices=["all", *GAME_DEFS.keys()], default="all")
    build.add_argument("--fill-missing", choices=["english", "blank"], default="english")
    build.set_defaults(func=cmd_build)

    term_report = sub.add_parser("term-report")
    term_report.set_defaults(func=cmd_term_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
