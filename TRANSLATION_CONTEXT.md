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
