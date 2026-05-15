#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESS_ROOT = ROOT.parent

GAMES = {
    "dow2": {
        "name": "Dawn of War 2",
        "en": PROCESS_ROOT / "Dawn of War 2" / "Locale" / "English" / "DOW2.ucs",
        "zh": PROCESS_ROOT / "Dawn of War 2" / "Locale" / "TChinese" / "DOW2.ucs",
    },
    "retribution": {
        "name": "Dawn of War II - Retribution",
        "en": PROCESS_ROOT / "Dawn of War II - Retribution" / "Locale" / "English" / "DOW2.ucs",
        "zh": PROCESS_ROOT / "Dawn of War II - Retribution" / "Locale" / "TChinese" / "DOW2.ucs",
    },
}

ID_LINE = re.compile(r"^(\d+)\t(.*)$")
ASCII_WORD = re.compile(r"[A-Za-z]{3,}")


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
        for bad in [item.strip() for item in avoid.split(";") if item.strip()]:
            result = result.replace(bad, preferred)
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
    for key, meta in GAMES.items():
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

    out = ROOT / "reports" / "coverage.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(out)


def cmd_export(args: argparse.Namespace) -> None:
    glossary = read_glossary(ROOT / "glossary" / "mainland_40k_tw.tsv")
    targets = GAMES.keys() if args.game == "all" else [args.game]
    for key in targets:
        meta = GAMES[key]
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        out = ROOT / "work" / f"{key}_translation.tsv"
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
    targets = GAMES.keys() if args.game == "all" else [args.game]
    for key in targets:
        meta = GAMES[key]
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        work = ROOT / "work" / f"{key}_translation.tsv"
        overrides: dict[str, str] = {}
        if work.exists():
            with work.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle, delimiter="\t"):
                    value = row.get("zh_new", "")
                    if value:
                        overrides[row["id"]] = value

        output = OrderedDict()
        for text_id, en_text in en.items():
            if text_id in overrides:
                output[text_id] = overrides[text_id]
            elif text_id in zh:
                output[text_id] = zh[text_id]
            elif args.fill_missing == "english":
                output[text_id] = en_text
            else:
                output[text_id] = ""

        out = ROOT / "output" / key / "Locale" / "TChinese" / "DOW2.ucs"
        write_ucs(out, output)
        print(out)


def cmd_term_report(args: argparse.Namespace) -> None:
    glossary = read_glossary(ROOT / "glossary" / "mainland_40k_tw.tsv")
    rows = []
    for key, meta in GAMES.items():
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

    out = ROOT / "reports" / "term_risks.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8-sig", newline="") as handle:
        fields = ["game_key", "id", "avoid_tw", "preferred_tw", "text"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Dawn of War II UCS translation pipeline")
    sub = parser.add_subparsers(required=True)

    report = sub.add_parser("report")
    report.set_defaults(func=cmd_report)

    export = sub.add_parser("export")
    export.add_argument("--game", choices=["all", *GAMES.keys()], default="all")
    export.set_defaults(func=cmd_export)

    build = sub.add_parser("build")
    build.add_argument("--game", choices=["all", *GAMES.keys()], default="all")
    build.add_argument("--fill-missing", choices=["english", "blank"], default="english")
    build.set_defaults(func=cmd_build)

    term_report = sub.add_parser("term-report")
    term_report.set_defaults(func=cmd_term_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
