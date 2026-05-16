# Dawn of War II Translation Context

This file is the persistent context for Codex workspace automation. Read it at
the start of every scheduled translation run, then update the progress and run
log sections before finishing.

## Project Goal

Rework the Traditional Chinese localization for:

- Warhammer 40,000: Dawn of War II - Anniversary Edition / Chaos Rising
- Warhammer 40,000: Dawn of War II - Retribution

The output must remain Traditional Chinese because the Steam language option is
TChinese, but the terminology and style should follow mainland Chinese
Warhammer 40,000 usage.

Primary working file:

```text
I:\translate_process\translation_project\work\manual_overrides.tsv
```

Build script:

```text
I:\Github\translate_dow2\scripts\ucs_pipeline.py
```

Process root:

```text
I:\translate_process
```

Output UCS files:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

## Style Rules

- Preserve Traditional Chinese characters.
- Translate against the English source, not only against the old TChinese text.
- Use natural mainland Warhammer 40,000 terminology while keeping Traditional
  Chinese glyphs.
- Preserve all placeholders, control tokens, punctuation variables, and line
  IDs exactly.
- Keep UI strings concise. Keep voice lines flavorful but not overly rewritten.
- If a line is ambiguous, prefer a conservative translation and add a note in
  `manual_overrides.tsv`.
- Do not invent lore terms when an established term exists.
- Treat Ork `Waaagh` / `WAAAGH` as a faction-specific war cry and
  cultural/psychic concept. Do not translate it as the generic cry `哇啊啊`.
  Use `WAAAGH！` for standalone shouts, and `WAAAGH` without punctuation in
  compounds such as `WAAAGH 能量`, `WAAAGH 戰旗`, `WAAAGH 點數`, and
  `WAAAGH 技能`.

## Required Terms

Use these forms unless a very specific context proves otherwise:

```text
Chaos = 混沌
Space Marines = 星際戰士
Imperial Guard / Astra Militarum = 星界軍
Eldar = 靈族
Orks = 獸人
Tyranids = 泰倫蟲族
Nurgle = 納垢
Khorne = 恐虐
Tzeentch = 奸奇
Slaanesh = 色孽
plasma = 等離子
missile = 導彈
Dreadnought = 無畏機甲
Wraith = 幽冥
Cyrus = 賽勒斯
Jonah Orion = 喬納·奧賴恩
Thule = 圖勒
Black Legion = 黑色軍團
Dark Gods = 黑暗諸神
Blood for the Blood God = 血祭血神
Skulls for the Skull Throne = 顱獻顱座
Warp Spider = 傳送蛛
Howling Banshee = 嚎叫女妖
missile launcher = 導彈發射器
lascannon = 激光炮
plasma cannon = 等離子炮
power armour = 動力裝甲
```

## Old Terms To Avoid

Scan for and replace these old or incorrect forms:

```text
神靈族
渾沌
歐克
毆克
白色標誌
太空陸戰隊
散彈機
散彈槍
偵查軍士
偵查態勢
毀滅之劍
默認
軍校
帝國衛隊
帝國衛兵
帝國防衛軍
防衛軍
世界末日號
異形蟲王
靈化腦蟲
無畏機兵
賽瑞斯
沙歷士
神靈術士
電漿
飛彈
冥靈
暗黑之神
腐敗之王
歐克蠻人
毆克蠻人
裘納
暗黑色軍團
次元蜘蛛
狂嚎女妖
火箭發射器
雷射砲
等離子大砲
動力盔甲
```

`異形` and `異星人` should usually become `異族`; in Tyranid-specific context
use `泰倫蟲族`, `泰倫生物`, or a more precise Tyranid term.

## Current Workflow

1. Read this file and `AUTOMATION_TASK.md`.
2. Inspect `manual_overrides.tsv` and the exported work TSV files under:

```text
I:\translate_process\translation_project\work
```

3. Add or refine entries in `manual_overrides.tsv`.
4. Build all UCS output files.
5. Verify output line counts, old term scan, residual English scan, and git
   status.
6. Update this file with the latest run summary.
7. Commit and push when there are meaningful workspace changes.

## Known Stable Output Counts

The latest successful heartbeat run reported:

```text
dow2 output UCS lines: 50695
retribution output UCS lines: 71720
old problem term scan: 0
```

Treat these as reference counts. If they change, explain why in the run log.

## Recent History

- A chat-bound heartbeat automation previously failed because Codex could not
  reliably resume the long chat thread. One failure used a stale path mismatch:
  normal Windows path versus `\\?\` extended Windows path.
- The 2026-05-17 03:27 JST heartbeat run completed successfully and rebuilt
  both output UCS files.
- The 2026-05-17 04:27 JST heartbeat run did not enter the chat at all. The
  automation was still active and the schedule was correct, so the likely fault
  was chat thread wakeup/resume, not the translation pipeline.
- The automation approach is now being moved to a workspace cron task so future
  runs do not depend on restoring this chat thread.

## Run Log

### 2026-05-17 06:09 JST

Main chat follow-up added the confirmed Ork `Waaagh` / `WAAAGH` terminology
rule to this context, to `AUTOMATION_TASK.md`, and to the active workspace
automation prompt. `Waaagh` should no longer be translated as the generic cry
`哇啊啊`; use `WAAAGH！` for standalone shouts and `WAAAGH` in compounds.

`I:\translate_process\translation_project\work\manual_overrides.tsv` was
normalized for this rule. Structured TSV verification found 0 remaining
`哇啊啊`, `WAAAGH?`, or lowercase `Waaagh` problems in the `zh_new` column
across 163 Waaagh-related rows.

The main chat rebuild succeeded and wrote both output UCS files. Output counts
remained stable: dow2 50695 lines, retribution 71720 lines. Old problem term
scan, including `哇啊啊` and `WAAAGH?`, returned 0 hits. Residual
same-as-English/ascii counts after the rebuild were dow2 136 and retribution
158.

### 2026-05-17 06:02 JST

Workspace automation run started at 05:37 JST and continued with active
translation, terminology, and audit work for more than 25 minutes. The run
updated `I:\translate_process\translation_project\work\manual_overrides.tsv`
with 471 new override rows. The largest groups were DOW2 residual Ork/combat/
Eldar/Scout voice cleanup, Retribution residual voice and Tyranid label cleanup,
flamer/lascannon/Carnifex terminology normalization, Waaagh voice consistency,
UI mixed-English labels, and subtitle cue localization.

The required UCS build was attempted after each batch, but every attempt failed
before writing outputs with `PermissionError: [Errno 13] Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
A direct non-destructive read/write open failed for both output UCS files, so
the output files were not updated during this scheduled run. The on-disk output
line counts remained stable: dow2 50695 lines, retribution 71720 lines.
On-disk old problem term scan remained 0 for both games; on-disk residual
same-as-English/ascii counts remained dow2 595 and retribution 265.

A no-write projected build using the updated manual override table produced the
stable counts dow2 50695 and retribution 71720, projected old problem term hits
0 for both games, projected residual same-as-English/ascii counts dow2 136 and
retribution 159, and projected contains-ascii counts dow2 1116 and retribution
1349. Today's new rows passed exact source/ID matching where applicable and
placeholder preservation checks. No stale `python`/`ucs_pipeline.py` child
process was found by the final process check. Committing the repository-side
context update was attempted, but Git could not create `.git/index.lock` due to
permission denial, so the context update remains uncommitted in the working
tree. `manual_overrides.tsv` is outside the repository and remains the primary
useful output for the run.

### 2026-05-17 05:31 JST

The 05:16 JST workspace automation run was interrupted by the user after it
used `Start-Sleep -Seconds 960` to pad runtime. The sleep runner was later
terminated from the main chat. The run had already made useful
`manual_overrides.tsv` progress before sleeping: it wrote a current-run batch
covering UI ability, targeting, prompt, objective, DOW2 map-name, wargear,
tutorial, achievement, shared label, NPC equipment, DOW2 Ork dialogue, and rich
presence cleanup entries. A quick count during the run reported 117 rows in
those current-run note categories.

The required UCS build still failed inside the cron context with
`PermissionError` on
`I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs`.
This is acceptable for future scheduled runs as long as
`manual_overrides.tsv` is updated; the main chat can rebuild UCS outputs later
from the latest override table. Automation instructions were updated to forbid
`sleep`, `Start-Sleep`, `timeout`, ping loops, or any idle waiting to satisfy
the minimum duration. The duration requirement now means active translation,
validation, audit, and cleanup work only.

### 2026-05-17 05:05 JST

Workspace automation run started at 04:54 JST and was stopped early at user
direction after repeated UCS write attempts failed. The run added 176
Retribution manual override rows for residual-English/missing voice and combat
strings, mainly Space Marine Terminator, Rhino/Razorback, Predator, Land
Raider, tactical order, capture, idle, and death barks around IDs 9028542-
9032194. It also covered the previously blocked missing strings 9075198,
9088824, and 9126793, and corrected the existing all-game override for 9075488
from `火箭發射器` to `導彈發射器`.

The required build command was attempted several times, including one final
explicit write attempt after user instruction, but still failed with
`PermissionError: [Errno 13] Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
A direct non-destructive ReadWrite open of the same UCS file also failed with
access denied, so the output UCS files were not updated.

Read-only verification against the current on-disk outputs: dow2 50695 lines,
retribution 71720 lines; current old-term scan found 1 DOW2 hit at ID 9075488
because the corrected override could not be rebuilt into the UCS output, and 0
Retribution hits. Current residual same-as-English/ascii scan: dow2 598,
retribution 268. A no-write projected pipeline check using the current override
table produced the stable line counts with projected old-term hits 0 for both
games and projected residual same-as-English/ascii counts dow2 595,
retribution 265. No stale pipeline child process remained by the final process
check.

Manual follow-up from the main chat at 05:08 JST used the same build command
outside the cron run and successfully rebuilt both UCS outputs. This confirms
that `ucs_pipeline.py`, the output files, and normal Windows ACLs are usable;
the earlier failure is most likely specific to the cron run's execution context
or a transient lock during that run. Verified output line counts stayed stable:
dow2 50695, retribution 71720. Old problem term scan returned 0 hits for both
rebuilt outputs.

### 2026-05-17 04:39 JST

Workspace automation run started at 04:39:59 JST but could not complete the
translation batch because the sandbox denied write access to
`I:\translate_process\translation_project\work\manual_overrides.tsv` and to the
generated output UCS files. A 20-line residual-English cleanup batch was
prepared for Retribution voice/objective/map strings around IDs 9075198,
9088824, 9124155-9126793, 9132668, 9140803, and 9142835, but it was not written.

Attempting the required build failed with `PermissionError: [Errno 13]
Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
Read-only verification against the existing outputs still matched the stable
counts: dow2 50695 lines, retribution 71720 lines. Old problem term scan: 0
terms hit in both outputs. Residual-English/ascii equality scan against current
outputs: dow2 599 same-as-English ascii entries, retribution 268
same-as-English ascii entries. No translation/output commit was possible because
the required translation/output files could not be changed. Committing this
run-log update was also attempted, but Git could not create `.git/index.lock`
due to permission denial, so the context update remains uncommitted in the
working tree.

The cause was the workspace cron configuration: it listed only
`I:\Github\translate_dow2` as its workspace directory, so the scheduled run could
not write outside that workspace to `I:\translate_process`. The cron automation
has now been updated to include both writable directories:

```text
I:\Github\translate_dow2
I:\translate_process
```

### 2026-05-17 04:35 JST

Created this persistent context file for workspace-based automation. The next
automation should read this file and `AUTOMATION_TASK.md` before translating,
then update this run log before finishing.
