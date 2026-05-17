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
  `WAAAGH 技能`. Keep a space before and after `WAAAGH` when it appears inside
  Chinese prose, unless adjacent to punctuation.
- Encoding safety rule: do not pass Traditional Chinese translation literals
  through a PowerShell here-string or pipeline into Python. The console code
  page can replace unsupported characters with literal `?` before Python sees
  them. Use `apply_patch` for repository Markdown, read translation batches
  from UTF-8/UTF-8-SIG files, or use Python `\uXXXX` escapes for non-ASCII
  string literals. After scripted TSV writes, scan the `zh_new` column for
  suspicious `?`, repeated `??`, `WAAAGH?`, and mojibake before building UCS.

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
Abaddon = 阿巴頓
Abaddon the Despoiler = 掠奪者阿巴頓
Dark Gods = 黑暗諸神
Blood for the Blood God = 血祭血神
Skulls for the Skull Throne = 顱獻顱座
Warp Spider = 躍遷蜘蛛
Howling Banshee = 嚎叫女妖
missile launcher = 導彈發射器
lascannon = 激光炮
plasma cannon = 等離子炮
power armour = 動力裝甲
Thaddeus = 撒迪厄斯
Kronus = 克羅努斯
Port Matthias = 馬提亞斯港
Armageddon = 阿米吉多頓
bolter = 爆彈槍
storm bolter = 風暴爆彈槍
heavy bolter = 重型爆彈槍
Eldritch Bolt = 靈能箭
Space Marine Captain = 連長
Battle Barge = 戰鬥駁船
Elena Derosa = 埃琳娜·德羅莎
Vandis = 范迪斯
Deimos = 戴莫斯
Gryphonne IV = 格里芬 IV
Kiwon = 基旺
Tranthios III = 特蘭西奧斯三號
Alpha Legion = 阿爾法軍團
Razorback = 剃刀背運兵車
Rhino = 犀牛運兵車
Predator = 掠食者 / 掠食者坦克
Warhammer 40,000: Dawn of War II = 戰鎚 40,000：戰爭黎明 II
Chaos Rising = 混沌崛起
Retribution = 懲罰
Rippa-Splitta = 殘虐裂手
Gorwazza = 戈瓦札
Blitzzagga = 布利札嘎
Deff Driva = 死駕
Hab Spire Legis = 萊吉斯居住尖塔
Astronomic Array = 天文陣列
Techpriest = 技術神甫
Mek / Mekboy = 技霸 / 技霸小子
Scout = 偵察兵
Tyrant Guard = 暴君守衛
Termagant = 槍蟲
Hormagaunt = 刀蟲
Carnifex = 卡尼菲克斯
Webway Assembly = 網道樞紐
Webway portal = 網道傳送門
Fire Prism = 火棱坦克
Prism Cannon = 火棱炮
Craftworld = 方舟世界
Soul Stone = 靈魂石
Stikkbombz = 棒槌炸彈
Slugga Boyz = 砍砍小子
Deff Dread = 死無畏
Looted Tank = 掠奪坦克
Ravener Alpha = 掘蟒蟲首領
Lictor Alpha = 利卡特首領
Synapse = 突觸
T'au / Tau castes = 鈦族，火氏族，土氏族，水氏族，以太氏族
Avatar of Khaine = 凱恩化身
Chaos Havocs = 混沌浩劫小隊
Plague Champion = 疫病冠軍
Aspiring Champion = 野心冠軍
Azariah Kyras = 阿扎賴亞·凱拉斯
Priam = 普里阿姆
Cyrene = 昔蘭尼
Commissar = 政委
Tarantula turret = 狼蛛炮塔
Space Hulk = 太空廢船
Judgment of Carrion = 腐屍審判號
Teleportarium = 傳送室
Capillary Tower = 毛細塔
biomass = 生物質
psychic power / spell = 靈能力；混沌巫術語境可用咒法/亞空間巫術
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
破曉之戰
混沌再起
掠奪者坦克
捕食者坦克
塔克斯
戴維恩
黎斯魯曼
荷瑪岡特
泰瑪岡特
火焰槍
惡魔王子
異端審判庭
老大頭領
胞子囊包
塔庫斯中位
星際終結者
次元蜘蛛
狂嚎女妖
火箭發射器
雷射砲
等離子大砲
動力盔甲
偵察兵盔甲
預設的盔甲
較輕的盔甲
魔法
法術
生體物質
威脅度
腐屍審判。
塔蘭圖拉
政戰委員
政戰軍委員
塞立尼
賽琳
運載工具
太空船
喬納‧歐里恩
克諾努斯
馬蒂亞斯港
突進跳躍
加乘
參予
強軔
機關槍
外星
祈禱者
葛麗芬
川希歐思
奇王
直戰團
攻擊攻擊
戴諾斯
阿法軍團
阿爾法戰團
艾雷那
迪羅沙
德羅沙
凡迪斯
技能開啟
能力開啟
武器開啟
可使用於
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

### 2026-05-17 19:53-20:04 JST

Main chat short active translation pass focused on repeated DOW2/Retribution
equipment tooltip cleanup in `scripts/ucs_pipeline.py`, then rebuilt both UCS
outputs after each batch. Scope: Mk VII/Mk VIII armor naming and descriptions,
Arbites Pattern III `Lawbringer` combat shotgun text, Astartes issue labels,
EMP/drone and retreat wording, DOW2 Space Marine weapon tooltip phrasing
(`Magnacore`, Mk V missile launcher, Mk IIs sniper rifle, Mk III sidearm,
Godwyn bolter, Mk X/Mk XI-c `Hell's Teeth` chainsword), and lore typo fixes
for Black Templars, Rogal Dorn, Tarsis Ultra, Deathwatch, Genestealer, and
Imperial Guard -> Astra Militarum wording.

Added stable terminology direction for visible equipment strings: use `Mk`
spacing consistently, `Mk VIII 游俠型`, `Mk VII 天鷹型`, `動力甲` for power armor
in item lore, `黑色聖堂`, `死亡守望`, `星界軍`, `基因竊取者`, `羅格·多恩`, and keep
weapon-pattern names as readable Traditional Chinese while retaining model
marks such as `Mk V`, `Mk X`, and `M35`.

Follow-up in the same pass cleared the remaining visible `阿斯塔特MK*`,
`MKVII/MKVIII`, `迷途類型`, `厚鈦板`, and `電力光纖束` scan hits to 0 in current
outputs.

### 2026-05-17 18:34-19:10 JST

Main chat active translation pass continued Retribution residual-English
cleanup while keeping output Traditional Chinese and mainland 40K terminology.
The pass primarily edited `scripts/ucs_pipeline.py` with durable phrase-level
final replacements, then rebuilt both game outputs after each batch.

Main cleanup groups: Imperial Guard and Scout combat barks, Tactical/Assault/
Devastator/Terminator/vehicle Space Marine voice variants, Predator/Rhino/
Razorback/Land Raider status lines, Eldar Guardian/Fire Prism/Banshee/Ranger/
Warp Spider/Farseer/Warlock/Wraithlord/Avatar lines, Ork Brakka/Nailbrain/
Sliksnik voice barks, map-specific Eldar/Ork encounter callouts, capture/
resource/victory-point system messages, allied hero incapacitated notices, and
many punctuation/case variants that previously remained same-as-English.

Terminology details kept in this pass: `星界軍`, `星際戰士`, `靈族`, `獸人`,
`泰倫蟲族`, `躍遷蜘蛛`, `幽冥骨`, `網道`, `方舟世界`, `火棱鏡`, `剃刀背`,
`蘭德掠襲者`, `終結者`, `WAAAGH`, `釘腦先生`, `司立克尼克`, and `布拉卡`.
The pass also corrected a lingering Retribution manual override for ID 9088769
from `有些小子想加入俺的哇啊！` to `有些小子想加入俺的 WAAAGH！`.

The build command succeeded and overwrote both UCS outputs:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Verification after rebuild: dow2 50695 lines, retribution 71720 lines, U+FFFD
0, known old-problem scan 0 hits, case-sensitive WAAAGH bad-form scan 0 hits
for `WAAAGH?`, `Waaagh`, `哇啊啊`, `獸人的WAAAGH`, `WAAAGH建築`,
`見識WAAAGH`, and `加入俺的WAAAGH`. Residual-English candidate scan still
has many rows remaining in Retribution, but this pass removed a large
contiguous block of battle VO and map-script English entries.

Follow-up before closing the same main-chat pass added another compact batch of
Eldar/Warlock/Banshee/Space Marine lines around IDs 9035350-9035470, including
Webway/shield calls, anti-Ork/anti-Tyranid map barks, allied commander callouts,
and drop-pod/refractor/teleport ability voice lines. Final quick validation
again kept dow2 50695 lines, retribution 71720 lines, U+FFFD 0, old-problem
scan 0, and WAAAGH bad-form scan 0.

### 2026-05-17 17:47-18:00 JST

Main chat active cleanup run. The pass continued using durable final
replacements in `scripts/ucs_pipeline.py`, because the remaining issues were
mostly repeated legacy phrases and malformed output text rather than isolated
manual override rows.

Main cleanup groups: DOW2/Retribution psychic wording (`靈能族敵軍`,
`靈能能量`, Warlock chain/psychic attack phrasing), Chaos campaign title text
(`尊爵` -> `升格者` / `升格之主` for Kyras' Ascendant title), UI and
mainland-style wording (`檢視` -> `查看`, `資訊` -> `信息`, `螢幕` ->
`屏幕`), Librarian terminology (`智庫館長` -> context-appropriate `智庫` or
`智庫館守護者`), Valkyrie/Imperial Guard/Tyranid bad backfills
(`瓦凱莉斯`, `星界軍騎兵`, `異形兵蟲`), damage/stat grammar
(`傷害至`, `裝甲等級至`, `反射所有傷害至攻擊者`), and character-name
normalization (`約拿`, `歐里恩`, `亞撒利雅`, `歐瑞安`,
`伊佳尼爾`).

Added targeted ID replacements for DOW2/Retribution lines where later source
backfills reintroduced malformed text, including Diomedes honor-guard lore
9132540 and Jonah Orion corruption relic lines 9133435, 9133439, and 9133444.

The build command succeeded and overwrote both UCS outputs:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Verification after rebuild: dow2 50695 lines, retribution 71720 lines, U+FFFD
0 for both outputs, suspicious `WAAAGH?` 0, known old-problem scan 0 hits. The
two `???` placeholder entries in each output remain unchanged legacy UI
placeholders rather than encoding loss.

### 2026-05-17 17:11-17:42 JST

Main chat active translation run. Work moved from row-by-row manual overrides
to durable final-replacement cleanup in `scripts/ucs_pipeline.py`, because the
remaining visible issues were repeated old TChinese phrases across both DOW2
and Retribution outputs. The run kept output in Traditional Chinese while using
mainland Warhammer 40K terminology.

Main cleanup groups: UI mainland wording (`點擊`, `鼠標`, `顯卡`, `局域網`,
`互聯網`, `補丁`, `個人檔案`), damage/vehicle phrasing (`傷害`, `受損`,
`載具`, `部署`), Cyrene / Inquisition lore (`昔蘭尼`, `審判官`,
`黑暗天使`, `大導師阿茲瑞爾`, `秘密之劍`), Retribution campaign terms
(`腐屍審判號`, `太空廢船`, `傳送室`, `政委`, `狼蛛炮塔`), Guard wording
(`星界軍士兵`, `星界軍步兵小隊`), Tyranid biomass/capillary-tower text
(`生物質`, `攝取生物質`, `毛細塔`), and psychic/sorcery wording
(`靈能力`, `咒法`, `亞空間巫術`) where the old text used generic
`魔法`/`法術`.

The build command succeeded repeatedly from the main chat and overwrote both
UCS outputs:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Follow-up verification should continue to scan the expanded old-term list,
encoding safety (`U+FFFD`, suspicious `?`, WAAAGH corruption), output line
counts, and git status before each closeout.

### 2026-05-17 16:45-17:05 JST

Main-chat translation cleanup rebuilt both games successfully. This pass added
script-level final replacements and validation coverage for vehicle terminology,
character names, UI title consistency, unlock requirement text, Tyranid/Ork unit
phrasing, and several obvious typo/grammar defects.

Key terminology and wording updates: `Predator -> 掠食者 / 掠食者坦克`,
`Tarkus -> 塔庫斯`, `Davian -> 戴維安`, `Leman Russ -> 黎曼魯斯`,
`Flamer -> 火焰噴射器`, `Daemon Prince -> 惡魔親王`,
`Dawn of War II -> 戰爭黎明 II`, `Chaos Rising -> 混沌崛起`,
`Nob Leader -> 老大頭目`, `Mycetic Spore -> 菌囊孢子`, and
`Mycetic Mine -> 菌囊地雷`. Also cleaned old/malformed strings including
`捕食者坦克`, `掠奪者坦克`, `塔庫斯中位`, `星際終結者`,
`胞子囊包`, `作業系統t`, `遭遇站`, and repeated Chinese question marks.

The final build command completed successfully and regenerated:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Verification: stable line counts, dow2 50695 and retribution 71720; Unicode
replacement characters 0; WAAAGH bad-form hits 0; generic `哇啊啊` hits 0;
expanded old-term scan returned 0 hits. The only remaining ASCII `??` instances
are the two original placeholder rows in each output (`511755`, `607755`).

### 2026-05-17 Razorback / Rhino Check

Main chat inspected the Retribution transport lines after the user reported
that the old `疣豬運兵車` icon now appears as `剃刀背運兵車`. The English source
for those UI and tutorial strings is `Razorback`, so the old Traditional
Chinese `疣豬` wording was incorrect. Confirmed current glossary direction:
`Razorback = 剃刀背`, `Rhino = 犀牛運兵車`. Added a final replacement for the bad
automation variant `剃刀鯨 -> 剃刀背` and rebuilt outputs.

### 2026-05-17 Abaddon Dialogue Fix

Main chat inspected Retribution dialogue and lore lines related to Abaddon.
Confirmed a bad automatic replacement had turned `艾班頓` into `艾小隊頓` in
current output. Added final replacements and manual override rows so Abaddon is
consistently `阿巴頓`, `Abaddon the Despoiler` is `掠奪者阿巴頓`, and
`Warmaster Abaddon` is `戰帥阿巴頓`. Rebuilt both UCS outputs successfully and
verified Retribution output has no remaining `艾小隊頓`, `艾班頓`, or raw English
`Abaddon` hits.

### 2026-05-17 14:19-14:38 JST

Main chat translation run started at 14:19:24 JST. The user later noted that
the current Codex quota was nearly exhausted, so the run was closed after the
active batch instead of continuing toward the earlier 40-minute target.

This batch covered early campaign dialogue polish, flank/objective phrasing,
WAAAGH mechanics and Ork voice prose, unlock and ability descriptions, Tau
caste/lore terminology, Eldar Craftworld/Soul Stone/Fire Prism/Warp Spider
terms, Ork Stikkbomb/Slugga/Deff Dread/Looted Tank terms, Tyranid
Carnifex/Ravener/Lictor/Synapse terms, and UI/stat wording such as health,
energy, resources, deployment, highlighting, wargear, and synchronized kills.
The appended manual override rows were also recorded in
`work_batches/2026-05-17-mainchat-ui-unit-lore-polish.tsv` for repository
tracking.

The build command completed successfully and regenerated both UCS outputs:
`I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs`
and
`I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs`.
Final verification: dow2 50695 lines, retribution 71720 lines, 0 Unicode
replacement characters, 0 `WAAAGH?`, and 0 hits from the expanded old-term
scan. The only repeated question-mark rows remaining are the original `???`
placeholder rows at IDs 511755 and 607755 in both games.

### 2026-05-17 13:29-14:00 JST

Main chat translation run. Started at 13:29:33 JST and continued active
translation, rebuild, and verification work through 14:00 JST before final
context/commit cleanup. The run updated `manual_overrides.tsv` through UTF-8
batch imports and expanded `FINAL_REPLACEMENTS` in `scripts/ucs_pipeline.py`
for high-confidence terminology normalization.

Main areas covered:

- DOW2 / Retribution Ork campaign terms: Rippa-Splitta, Gorwazza, Blitzzagga,
  Deff Driva, Green Tooth Gorge, Mek / Mekboy.
- Typhon Astronomic Array and Techpriest wording: `天文陣列`,
  `技術神甫`, `技霸`, `殘虐裂手`.
- Hab Spire Legis and cargo-bay objective text.
- Repeated old terms and typo cleanup: `疣豬運兵車 -> 剃刀背運兵車`,
  `新進者 -> 新兵`, `士官 -> 軍士`, `菁英 -> 精英`,
  `網絡聯集 -> 網道樞紐`, `網絡傳送門 -> 網道傳送門`,
  `特馬根 -> 槍蟲`, `賀馬根 -> 刀蟲`,
  `蟲王護衛 -> 暴君守衛`, `滅絕者 -> 浩劫者/浩劫小隊`,
  `亞薩利亞 -> 阿扎賴亞`, `普萊安 -> 普里阿姆`.
- Encoding/punctuation cleanup: old `‧` name separator to `·`, duplicated
  `的的`, `小隊小隊`, `進行進行`, `。。`, malformed `亞拉哈斯t-`,
  and `卡尼菲克斯斯`.

Build command completed successfully and rewrote both output UCS files:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Verification at 14:00 JST: line counts remained stable, dow2 50695 and
retribution 71720. `rg` scan against the expanded old-term list returned no
hits. Encoding scan found U+FFFD 0 and WAAAGH? 0 in both outputs; the only
`??` matches are the known original placeholder rows.

Follow-up before closing this run added rule-level WAAAGH spacing and
punctuation normalization to `FINAL_REPLACEMENTS`, covering old forms such as
`WAAAGH!`, `獸人WAAAGH`, `消耗WAAAGH`, `引導WAAAGH`, and
`困在WAAAGH中`. The build script also now normalizes ASCII `!` to full-width
`！` when the mark is adjacent to Chinese text.

### 2026-05-17 13:13-13:28 JST

Main chat ran another active manual translation pass after the user requested a
40-minute target. The run started at 13:13:52 JST. The pass focused on
high-confidence cleanup rather than idle waiting, and ended after repeated
build/scan cycles found no further ordinary text targets beyond internal UI and
developer placeholders.

The run updated
`I:\translate_process\translation_project\work\manual_overrides.tsv` to 67330
rows and rebuilt both UCS outputs successfully. New batches under
`I:\Github\translate_dow2\work_batches` covered DOW2 Tyranid/xenos readable
lines, DOW2 game-specific override refreshes, Space Marine `Captain` rank
cleanup, wargear and lore descriptions, Thur'Abis/Deimos/Kiwon/Gryphonne
terminology, Alpha Legion correction, Elena Derosa briefing text, and the two
remaining ordinary `Die.` voice/text entries. `scripts\ucs_pipeline.py` gained
additional final replacements for stable UI and terminology normalization such
as `能力開啟 -> 能力解鎖`, `上尉 -> 連長` in Space Marine contexts, `戴諾斯 ->
戴莫斯`, `艾雷那/迪羅沙/凡迪斯` normalization, and `MK Iva -> MK IVa`.

The build command succeeded and wrote:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Verification after rebuild: dow2 50695 lines, retribution 71720 lines. Expanded
old-term scans returned 0 hits for both outputs. Encoding scan found 0 `U+FFFD`,
0 `WAAAGH?`, and only the two original `???` placeholder rows. Residual
same-as-English ASCII scan after filtering leaves only internal UI/resource
labels, rich-presence placeholders, developer strings, or Tau sept names.

### 2026-05-17 12:20-13:00 JST

Main chat continued the manual translation pass after the user deleted the
scheduled automation. Work started at 12:20:26 JST and continued through the
main-chat batch loop. The run updated
`I:\translate_process\translation_project\work\manual_overrides.tsv` to 67250
rows and rebuilt both UCS outputs successfully.

Main translation cleanup covered WAAAGH mechanics/dialogue, Tyranid readable
lines, Armageddon ship references, Eldar and xenos wording, visible question
mark punctuation, Jonah Orion/Thaddeus/Kronus/Port Matthias consistency,
Armageddon War wording, Imperial Guard wording, `bolter`/`heavy bolter`
misrendered as `機關槍`, and the Martellus/Tarkus heresy outcome lines around
IDs 9133724 and 9133728. New work batch files were written under
`I:\Github\translate_dow2\work_batches`, and `scripts\ucs_pipeline.py` gained
additional final replacement rules for stable terminology normalization.

The build command succeeded and wrote:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Verification after rebuild: dow2 50695 lines, retribution 71720 lines. The
expanded old-problem scan returned 0 hits for both outputs, including
`喬納‧歐里恩`, `克諾努斯`, `馬蒂亞斯港`, `突進跳躍`, `加乘`, `參予`, `強軔`,
and `機關槍`. Encoding scan found 0 `U+FFFD`, 0 `WAAAGH?`, 0 bad WAAAGH point
forms, and 0 `觸發?` artifacts. Remaining same-as-English ASCII hits are
internal UI/test labels, placeholder voice tags, copyright text, or similar
non-translation strings.

### 2026-05-17 11:59 JST

Main chat checked the current automation-updated
`I:\translate_process\translation_project\work\manual_overrides.tsv` and rebuilt
both UCS outputs. The TSV has 68943 rows with the expected columns
`game_key`, `id`, `en`, `zh_new`, and `notes`; `zh_new` has 0 empty values.
The 299 non-numeric `id` rows are expected `game_key=all` source-text override
rows rather than corruption. Structured TSV checks found 0 old problem term
hits, 0 `WAAAGH` rule violations, and 0 CJK rows containing suspicious literal
`?` corruption.

The main chat build command succeeded and wrote:

```text
I:\translate_process\translation_project\output\dow2\Locale\TChinese\DOW2.ucs
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Output verification after rebuild: dow2 50695 lines, retribution 71720 lines.
Old problem term scan returned 0 hits for both games. Residual
same-as-English/ascii counts are dow2 80 and retribution 104; contains-ascii
counts are dow2 1114 and retribution 1348. A CJK-plus-ASCII-question-mark scan
reported 17 dow2 rows and 8 retribution rows; sampled hits were normal question
punctuation or explicit `?` UI marker text, not the earlier PowerShell encoding
replacement issue.

### 2026-05-17 11:54 JST

Workspace automation run started after reading this context and
`AUTOMATION_TASK.md`, then continued with active translation, source validation,
duplicate audits, projected-output scans, and repeated build verification until
approximately 11:54 JST. The run appended 294 current-run rows to
`I:\translate_process\translation_project\work\manual_overrides.tsv`.

The translated groups were DOW2 Tyranid/alien/xenos terminology cleanup across
campaign dialogue, objectives, infestation/tutorial text, synapse descriptions,
capillary tower abilities, and endgame/campaign-system strings; DOW2 Ork
booby-trap and late Tyranid campaign cleanup; and Retribution early Ork/Feral
Ork tutorial, objective, wargear, and voice text cleanup. The run used
source-bound append-only supersession rows so newer exact-source entries beat
older direct or source override text.

Current-run structured validation found 0 source mismatches across the 294
rows: 238 DOW2 rows and 56 Retribution rows. `zh_new` corruption scans found 0
literal `?`, 0 repeated `??`, 0 `WAAAGH?`, 0 Unicode replacement characters,
0 known mojibake patterns, and 0 generic `哇啊啊` WAAAGH translations.
Current-run duplicate-key audit found 0 duplicate `game_key`/`id` keys. The
duplicate-source audit found 7 repeated current-run source texts, all expected
repeated labels or duplicate tooltip strings such as Ork Booby Trap, Tyranids
in Synapse, and repeated capillary tower descriptions.

The required UCS build was attempted after the first translation batch, again
after the Retribution cleanup batch, and again during final verification. Every
attempt failed before writing outputs with `PermissionError: [Errno 13]
Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
The output UCS files were therefore not updated during this run; the updated
manual override table remains the useful output.

Current on-disk output counts remained stable: dow2 50695 lines, retribution
71720 lines. A no-write projected build using the updated manual override table
also produced stable counts: dow2 50695 and retribution 71720. Projected
same-as-English/ascii counts remained dow2 80 and retribution 104; projected
contains-ascii counts remained dow2 1114 and retribution 1348. Projected old
problem term scan from the required context list found 0 hits for both games,
and projected WAAAGH bad-form scan found 0 hits for both games. A broader
contextual Ork/Tyranid/alien worklist scan still found DOW2 542 and
Retribution 218 rows, mostly remaining Feral Ork/Ork and Tyranid cleanup
candidates outside this run's completed batches.

No live `python.exe` processes were reported by the final process check. Plain
`git status` failed under the sandbox user because Git detected dubious
ownership for `I:\GitHub\translate_dow2`; running Git with
`-c safe.directory=I:/GitHub/translate_dow2` showed branch `main` and
`TRANSLATION_CONTEXT.md` modified before this entry. Commit/push was attempted
after this entry.

### 2026-05-17 10:55 JST

Workspace automation run started at approximately 10:38 JST and continued with
active shared UI cleanup, DOW2/Retribution glossary supersession, source
validation, duplicate audits, projected-build checks, output scans, and build
verification until approximately 10:55 JST. The run appended 373 current-run
rows to
`I:\translate_process\translation_project\work\manual_overrides.tsv`.

The translated groups were shared multiplayer/social UI strings for leaving,
joining, invitations, friend/ignore lists, matchmaking, chat whispers, map
changes, ranking prompts, and visible campaign/status strings; DOW2 targeted
glossary cleanup for Greenskin/Ork, Carnifex, Mekboy, Heavy Flamer, Librarian,
and Lascannon/Tarantula turret strings; and Retribution targeted glossary
cleanup for Mekboy, Carnifex, Librarian/Jonah Orion, Greenskin voice barks,
Lascannon/Tarantula turret labels and descriptions, and flamer tutorial text.
The run used append-only supersession rows so newer source-matched terminology
beats older direct or source override text.

Current-run structured validation found 0 source mismatches across the 373
rows. Placeholder validation found 0 mismatches. `zh_new` corruption scans
found 0 literal `?`, 0 repeated `??`, 0 `WAAAGH?`, 0 Unicode replacement
characters, and 0 generic `哇啊啊` WAAAGH translations in current-run rows.
Current-run duplicate audit found 0 duplicate `game_key`/`id` keys; 64 duplicate
current-run source texts were expected repeated labels or cross-game voice/UI
strings.

The required UCS build was attempted after the first batch, after follow-up
translation batches, and again during final verification. Every attempt failed
before writing outputs with `PermissionError: [Errno 13] Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
The output UCS files were therefore not updated during this run.

Current on-disk output counts remained stable: dow2 50695 lines, retribution
71720 lines. Current on-disk old problem term scan from this context found 0
hits for both games. A no-write projected build using the updated manual
override table produced stable counts dow2 50695 and retribution 71720.
Projected same-as-English/ascii counts were dow2 80 and retribution 104;
projected contains-ascii counts were dow2 1114 and retribution 1348. The
projected targeted glossary scan for Ork/Greenskin, Carnifex, Mekboy,
Librarian, Flamer, and Lascannon now shows DOW2 2 rows and Retribution 222 rows
remaining after this run's supersession batches. Projected context old-term
scan showed DOW2 735 rows and retribution 0 rows; the DOW2 number remains a
broad projected-worklist measure rather than an on-disk output regression.

No live `python` processes were reported by the final process check. Repository
status still showed only `TRANSLATION_CONTEXT.md` modified before this entry.
Commit/push was attempted after this entry, but Git failed to create
`.git/index.lock` due to permission denial, so push was not attempted. The
primary useful output of the run is the updated `manual_overrides.tsv` outside
the repository; the latest override table can be used for a manual UCS rebuild
from the main chat.

### 2026-05-17 10:04 JST

Workspace automation run started at approximately 09:38 JST and continued with
active shared voice translation, DOW2/Retribution glossary supersession,
projected-build checks, source validation, duplicate audits, output scans, and
git/process verification until approximately 10:04 JST. The run appended 556
current-run rows to
`I:\translate_process\translation_project\work\manual_overrides.tsv`.

The translated groups were shared Space Marine combat/selection barks around
9028539-9034067, DOW2 Flamer/Ork/Eldar/Carnifex/Librarian terminology cleanup,
DOW2 flamer equipment and tutorial strings, DOW2 Carnifex objective and wargear
labels, Retribution direct supersession rows for Ork/Greenskin mission barks,
Retribution flamer/Sentinel equipment lines, and Retribution Carnifex/Librarian
campaign text. The run used append-only duplicate supersession rows where older
direct overrides would otherwise beat newer source-matched terminology. A
Python in-place rewrite attempt for broad existing override normalization failed
with `PermissionError` on `manual_overrides.tsv`, so the run used `apply_patch`
append supersession rows instead.

Current-run structured source validation found 0 source mismatches across the
556 rows. `zh_new` corruption scans found 0 literal `?`, 0 repeated `??`, 0
`WAAAGH?`, and 0 known WAAAGH mojibake hits. Current-run duplicate audit found
0 duplicate current-run `game_key`/`id` keys; 27 duplicate current-run source
texts were deliberate repeated barks or labels.

The required UCS build was attempted after each translation batch and again
during final verification. Every attempt failed before writing outputs with
`PermissionError: [Errno 13] Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
The output UCS files were therefore not updated during this run.

Current on-disk output counts remained stable: dow2 50695 lines, retribution
71720 lines. Current on-disk old problem term scan from this context found 0
hits for both games. Current on-disk bad WAAAGH scan found 0 hits for both
games. Current on-disk ascii-only-with-letters counts were dow2 264 and
retribution 287; contains-ascii counts were dow2 1156 and retribution 1399.

A no-write projected build using the updated manual override table produced
stable counts dow2 50695 and retribution 71720. Projected same-as-English/ascii
counts were dow2 164 and retribution 191; projected contains-ascii counts were
dow2 1034 and retribution 1244. The filtered context old-term scan showed
projected retribution 0 rows and DOW2 727 rows. A narrower targeted glossary
scan for Orks/Ork, Carnifex, Zoanthrope, Librarian, Flamer, and Eldar showed
projected DOW2 42 hits and retribution 225 hits after this run's supersession
batches. Projected WAAAGH bad-form scan found 0 hits.

No live `python` processes were reported by the final process check. Repository
status still showed only `TRANSLATION_CONTEXT.md` modified before this entry.
Commit was attempted after this entry, but Git failed to create
`.git/index.lock` due to permission denial, so push was not attempted. The
context update remains uncommitted in the working tree, and the primary useful
output of the run remains the updated `manual_overrides.tsv` outside the
repository.

### 2026-05-17 08:58 JST

Workspace automation run started at approximately 08:40 JST and continued with
active WAAAGH terminology cleanup, DOW2 old-term translation batches,
source-validation checks, projected-build checks, output scans, and git/process
verification until approximately 08:58 JST. The run appended 145 current-run
rows to
`I:\translate_process\translation_project\work\manual_overrides.tsv`.

The translated groups were Retribution WAAAGH compound punctuation cleanup for
banner, meter, points, ability, and cultural-concept lines; DOW2 Dreadnought,
plasma, Zoanthrope, missile launcher, Cyrus/Armageddon, Hive Tyrant, Warlock,
and Dark Gods terminology cleanup. Current-run structured source validation
found 0 source mismatches across the 145 rows. `zh_new` corruption scans found
0 literal `?`, 0 repeated `??`, 0 `WAAAGH?`, and 0 known WAAAGH mojibake hits.
Projected WAAAGH compound punctuation checks found 0 remaining `WAAAGH！ `
compound hits for both games.

The required UCS build was attempted after the WAAAGH batch, after the DOW2
old-term batch, after the Cyrus/missile batches, and again during final
verification. Every attempt failed before writing outputs with
`PermissionError: [Errno 13] Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
The output UCS files were therefore not updated during this run.

Current on-disk output counts remained stable: dow2 50695 lines, retribution
71720 lines. Current on-disk old problem term scan remained 0 for both games.
Current on-disk same-as-English/ascii counts were dow2 145 and retribution 168.
A no-write projected build using the updated manual override table produced
stable counts dow2 50695 and retribution 71720, projected WAAAGH compound or
question-mark hits 0 for both games, projected generic `哇啊啊` WAAAGH
translation hits 0 for both games, projected same-as-English/ascii counts dow2
89 and retribution 114, and projected contains-ascii counts dow2 1115 and
retribution 1348. The projected old-term scan now shows retribution 0 rows and
DOW2 730 rows, reduced by this run's DOW2 terminology batches.

Final process inspection found one `python` process using the Codex runtime
interpreter, but querying its command line with `Get-CimInstance` was denied by
the environment, so it was not identified as a stale `ucs_pipeline.py` child and
was not stopped. Repository commit was attempted after this entry, but Git
failed to create `.git/index.lock` due to permission denial, so push was not
attempted. The context update remains uncommitted in the working tree, and this
run's primary useful output remains the updated `manual_overrides.tsv` outside
the repository.

### 2026-05-17 07:58 JST

Workspace automation run started at approximately 07:38 JST and continued with
active translation, source validation, projected-build checks, output write
probes, residual-English triage, duplicate audits, and old-term scans until
approximately 07:58 JST. The run appended 217 current-run rows to
`I:\translate_process\translation_project\work\manual_overrides.tsv`.

The translated groups were shared chat and lobby labels, multiplayer
`Label_Value` cleanup, shared numeric/unit UI strings, installer UI strings,
Tyranid terminology, shared unit labels around 9120325-9120363, DOW2
campaign/old-term cleanup for Armageddon/Dreadnought/plasma/missile/Cyrus
strings, and repeated exact-source cleanup for DOW2/Retribution labels and
descriptions involving Cyrus, Jonah, Wraithlord, Wraithguard, Warlock, Black
Legion, Dark Gods/Lord of Decay, Dreadnought, missile, plasma, Hive Tyrant, and
Zoanthrope terminology. Current-run structured source validation found 0 source
mismatches after corrections. `zh_new` corruption scans found 0 literal `?`, 0
repeated `??`, 0 `WAAAGH?`, 0 lowercase `Waaagh`, and 0 generic `哇啊啊` hits.
The manual override old-term scan found 0 hits after correcting an existing
`igguy` row from `帝國衛兵` to `星界軍士兵` and the new shared Dreadnought row
from `無畏機兵` to `無畏機甲`.

The required UCS build was attempted repeatedly after translation batches and
again during final verification. Every attempt failed before writing outputs
with `PermissionError: [Errno 13] Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
A direct read/write probe also failed for both current output UCS files with
`PermissionError`, so the output UCS files were not updated during this run.
There were no stale `python`/`ucs_pipeline.py` child processes found.

Current on-disk output counts remained stable: dow2 50695 lines, retribution
71720 lines. Current on-disk old problem term scan remained 0 for both games.
A no-write projected build using the updated manual override table produced the
stable counts dow2 50695 and retribution 71720, projected old problem term hits
0 for both games, projected same-as-English/ascii counts dow2 80 and
retribution 104, and projected contains-ascii counts dow2 1102 and retribution
1344. The remaining projected same-as-English/ascii rows are mostly UI/control
tokens, test strings, URLs, hardware labels, or deliberate code-like strings.
Duplicate key audit still found 824 duplicate `game_key`/`id` keys overall;
none of this run's current-run rows were on duplicate keys. Repository commit
was attempted after this entry, but Git again failed to create
`.git/index.lock` due to permission denial, so push was not attempted. The
context update remains uncommitted in the working tree.

### 2026-05-17 06:45 JST

Workspace automation run started at approximately 06:19 JST and continued with
active translation, validation, projected-build checks, duplicate audits, and
terminology scans until 06:45 JST. The run appended 212 new rows to
`I:\translate_process\translation_project\work\manual_overrides.tsv`.

The translated groups were shared Space Marine movement/combat barks, DOW2
Predator/Razorback/Rhino/Land Raider vehicle lines, Retribution short Ork and
Space Marine transport lines around IDs 9026216-9032808, subtitle cue labels
around 9090476-9119812, and shared UI/multiplayer placeholder cleanup around
10250, 38070-43450, and 146709-146749. Structured checks found 0 source
mismatches for the new rows, 0 placeholder mismatches in the UI batch, and 0
`?`, repeated `??`, `WAAAGH?`, `Waaagh`, or `蜩・賦蝠柿` corruption hits in
`zh_new`.

The required UCS build was attempted after translation batches, but both
attempts failed before writing outputs with `PermissionError: [Errno 13]
Permission denied:
'I:\\translate_process\\translation_project\\output\\dow2\\Locale\\TChinese\\DOW2.ucs'`.
The output UCS files were therefore not updated during this run. Current
on-disk output counts remained stable: dow2 50695 lines, retribution 71720
lines. Current on-disk old problem term scan remained 0 for both games.

A no-write projected build using the updated manual override table produced the
stable counts dow2 50695 and retribution 71720, projected old problem term hits
0 for both games, projected same-as-English/ascii counts dow2 191 and
retribution 216, projected contains-ascii counts dow2 1412 and retribution
1839, and projected strong same-as-English/ascii residuals dow2 2 and
retribution 10 under the current triage heuristic. The strong missing-English
work-file scan returned 0 remaining strong candidates for both games after the
new overrides. Duplicate override audit still found 823 pre-existing duplicate
`game_key`/`id` keys; none were introduced by this run's appended rows.
Repository commit was attempted after this entry, but Git again failed to create
`.git/index.lock` due to permission denial, so push was not attempted.
`manual_overrides.tsv` remains the primary useful output outside the repo.

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

### 2026-05-17 18:01-18:31 JST

Main-chat translation pass continued with active translation work only. The
pass edited `scripts/ucs_pipeline.py` and rebuilt both UCS outputs repeatedly
with `ucs_pipeline.py --process-root I:\translate_process build --game all
--fill-missing english`.

Scope covered in this pass:

- Mainland terminology cleanup for UI/system text: `計劃`, `賬號`, `視頻`,
  `全局`, `窗口`, `服務器`, `在線`, `多人聯機`, `個人資料`, `文件`,
  `硬件`, `顯存`, `紋理`, `作弊`, `自定義`, and targeted `質量` settings.
- Warp/Eldar/DOW2 cleanup: `亞空間`, `躍遷蜘蛛`, `聚焦亞空間爆破`,
  `亞空間之火`, `群體亞空間傳送`, and better DOW2 artillery/Warp text.
- Ork and Tyranid cleanup: `WAAAGH` kept untranslated; `砍砍小子`,
  `槍槍小子`, `大槍小子`, `鐵皮蝦米`, `劊子獸`, `蟲巢暴君`,
  `泰倫蟲族正在行動`.
- Chaos/lore cleanup: `黑暗諸神`, `黑暗科技時代`, `黑暗聖戰`,
  `黑暗靈族`, `暗鴉守衛`, `黑色圖書館`, `懷言者軍團`,
  `吞世者`, `放血鬼`, `黑暗傳送門`, `黑暗光環`.
- DOW2/Retribution residual-English cleanup: added large all-game English
  phrase mappings for Space Marine/Tarkus tactical barks, capture/order barks,
  base warning lines, victory/defeat lines, reinforcements, and wargear
  equipment prompts around IDs 9025573-9027406.
- Fixed several visible bad lines: Ork Mek no longer `闇影者`, `白色烙印`
  now `白色疤痕`, `圖爾連長` now `圖勒連長`, and the Thule toxin lines now
  avoid `擊殺圖勒連長的毒素`.

Rule notes preserved for future work: keep Traditional Chinese glyphs but use
mainland 40K terminology; keep `WAAAGH` as `WAAAGH`; Razorback remains
`剃刀背`; Bane Wolf remains `毒狼`; Bloodletter is now standardized as
`放血鬼`.

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
