# Workspace Automation Task

Read `TRANSLATION_CONTEXT.md` before doing any translation work. This scheduled
task exists because chat-bound heartbeat automation was unreliable for this long
conversation.

## Runtime Target

- Record the Tokyo start time at the beginning of every run.
- After each small translation batch, check the Tokyo time again.
- If total elapsed time is under 25 minutes, continue with another batch.
- Do not use `sleep`, `Start-Sleep`, `timeout`, ping loops, or any idle waiting
  to satisfy the minimum duration.
- The minimum duration means active work time. Keep finding, translating,
  validating, deduplicating, and writing useful `manual_overrides.tsv` changes
  until the elapsed time reaches the target.
- If no strong translation candidates remain, spend the remaining active time on
  terminology consistency checks, duplicate override audits, residual-English
  triage, old-term scans, and context cleanup. Do not idle.
- Stop after at least 25 minutes of active work, then verify and summarize.

## Translation Work

Use `I:\translate_process` as the process root. Continue editing:

```text
I:\translate_process\translation_project\work\manual_overrides.tsv
```

You may advance both `dow2` and `retribution` in the same run. Prioritize:

- residual English strings
- obviously wrong old translations
- old forbidden terms listed in `TRANSLATION_CONTEXT.md`
- UI strings visible to players
- campaign, wargear, ability, race, squad, and voice-line text where English and
  old TChinese disagree

Keep all text Traditional Chinese with mainland Warhammer 40,000 terminology.

Terminology rule for Ork `Waaagh` / `WAAAGH`: keep it as the faction-specific
war cry and cultural/psychic concept. Do not translate it as the generic cry
`哇啊啊`. Use `WAAAGH！` for standalone shouts, and `WAAAGH` without punctuation
in compounds such as `WAAAGH energy`, `WAAAGH banner`, `WAAAGH points`, or
`WAAAGH ability`.

## Encoding Safety

When editing `manual_overrides.tsv`, avoid any workflow that sends Traditional
Chinese text through a PowerShell here-string or pipeline into Python, because
the Windows console code page may replace unsupported characters with literal
`?` before Python receives them.

Use one of these safer methods instead:

- edit repository Markdown files with `apply_patch`
- read translations from an existing UTF-8/UTF-8-SIG file
- use Python string `\uXXXX` escapes for non-ASCII translation literals
- use the bundled Python executable and open TSV files with
  `encoding="utf-8-sig"` and `newline=""`
- use `csv.DictReader` / `csv.DictWriter` with tab delimiters for TSV changes

After every scripted TSV write, run a structured check on the `zh_new` column
for suspicious corruption such as literal `?`, repeated `??`, `WAAAGH?`, and
known mojibake patterns. If corruption is found, fix it before building UCS
outputs or committing context updates.

## Build Command

Attempt this after each batch:

```powershell
C:\Users\mikez\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe I:\Github\translate_dow2\scripts\ucs_pipeline.py --process-root I:\translate_process build --game all --fill-missing english
```

This normally updates:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

If the cron run cannot write the output UCS files, record the failure clearly
and keep treating successful `manual_overrides.tsv` updates as useful progress.
The UCS files can be rebuilt later from the main chat using the latest manual
override table.

## Verification

Before finishing every run, check:

- output UCS line counts for both games
- old problem term scan
- residual English scan
- `git status`
- whether `manual_overrides.tsv` and output files were updated as expected

Do not force-kill Codex or the scheduled job. If there are leftover child
processes from the translation pipeline, report them. Only stop clearly stale
`python`, `git`, or `ucs_pipeline.py` child processes if they belong to the
current translation run and are still running after the build has completed.

## Context Update

Before finishing every run, update `TRANSLATION_CONTEXT.md`:

- append a short dated run-log entry
- mention the main ranges or categories translated
- record output line counts
- record old-term and residual-English scan results
- record whether a commit/push was made
- update any newly confirmed terminology decisions

## Git

Commit and push when there are meaningful changes. Use a concise commit message
in Chinese or English, for example:

```text
Update DOW2 localization overrides
```

No extra user confirmation is required for commit or push.

## Final Report

The run summary should include:

- Tokyo start time
- Tokyo end time
- total elapsed time
- modified files or translation categories
- output UCS paths
- verification result
- commit/push result, if applicable
