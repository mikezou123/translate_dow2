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

Current user direction as of 2026-05-18: DOW2 / Chaos Rising has been cleared
in-game, so do not actively spend translation passes on DOW2 unless the user
explicitly asks. Continue active translation and QA on Retribution.

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
Venerable Dreadnought = 尊者無畏機甲
Wraith = 幽冥
Wraithlord = 幽冥領主
Cyrus = 賽勒斯
Jonah Orion = 喬納·奧賴恩
Thule = 圖勒
Black Legion = 黑色軍團
Abaddon = 阿巴頓
Abaddon the Despoiler = 掠奪者阿巴頓
Dark Gods = 黑暗諸神
Blood for the Blood God = 血祭血神
Skulls for the Skull Throne = 顱獻顱座
Warp Spider = 躍遷蛛
Howling Banshee = 嚎叫女妖
missile launcher = 導彈發射器
lascannon = 激光炮
plasma cannon = 等離子炮
Fusion Gun = 熱熔槍
Fusion Blaster = 熱熔爆破槍
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
Land Raider = 蘭德掠襲者
Warhammer 40,000: Dawn of War II = 戰錘 40,000：戰爭黎明 II
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
Big Mek = 大技霸
Dakka = 噠咔
Artificer Power Armor = 精工動力甲
Scout = 偵察兵
Sentinel = 哨衛機甲
Tyrant Guard = 暴君守衛
Termagant = 槍蟲
Hormagaunt = 刀蟲
Carnifex = 卡尼菲克斯
Webway Assembly = 網道樞紐
Webway portal = 網道傳送門
Fire Prism = 火稜鏡坦克 / 火稜鏡
Prism Cannon = 火稜鏡炮
Craftworld = 方舟世界
Soul Stone = 靈魂石
Stikkbombz = 棒槌炸彈
Slugga Boyz = 砍砍小子
Shoota Boyz = 槍小子
Kommando = 特戰小子
Kommando Nob = 特戰老大
Nob Leader = 老大頭目
Wartrukk = 戰爭卡車
Deff Dread = 死亡無畏
Looted Tank = 掠奪坦克
Ravener = 掘蟒
Ravener Alpha = 掘蟒阿爾法
Ripper = 撕裂蟲
Zoanthrope = 靈能蟲
Lictor Alpha = 利卡特阿爾法
Synapse = 突觸
Bio-toxin = 生物毒素
Biomorph = 生體變異
Hive Fleet Leviathan = 利維坦蟲巢艦隊
Hive Fleet Behemoth = 貝希摩斯蟲巢艦隊
Hive Fleet Kraken = 克拉肯蟲巢艦隊
Tarsis Ultra = 塔西斯·奧特拉
Ultramar = 奧特拉瑪
T'au / Tau castes = 鈦族，火氏族，土氏族，水氏族，以太氏族
Exarch = 司戰
Avatar of Khaine = 凱恩戰神分身
Khaine = 凱恩
Wraithguard = 幽冥守衛
Chaos Havocs = 混沌浩劫小隊
Plague Champion = 瘟疫冠軍
Blastmaster = 爆裂大師
Aspiring Champion = 野心冠軍
Bloodcrusher = 碾血者
Araghast the Pillager = 掠奪者亞拉哈斯特
Ulkair = 烏凱爾
Selenon = 塞勒農
The Ice Works = 冰工廠
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
Pheromone = 信息素
Mycetic Spore / Spore Drop = 菌囊孢子
psychic power / spell = 靈能力；混沌巫術語境可用咒法/亞空間巫術
Swarmlord = 蟲群之主
Servitor = 機僕（機械教/星際戰士構造體語境）；Retinue/entourage 不要誤改為機僕
Caliban = 卡利班
Vulkan = 伏爾甘
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
角蟲
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
蘭德掠襲者
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

### 2026-05-22 22:45-23:25 JST

Main-chat Retribution-only terminology and QA pass. DOW2 / Chaos Rising was not
actively targeted because the user has already cleared DOW2 in-game. The pass
edited `scripts/ucs_pipeline.py`, refreshed current terminology rules in this
context file, and rebuilt only:

```text
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Scope covered:
- Space Marine and vehicle cleanup: `Drop Pod = 空降艙`,
  `Tactical Dreadnought Armor = 終結者裝甲`, `Assault Squad =
  突擊星際戰士小隊`, `Iron Halo = 鋼鐵光環`, `Rosarius = 玫瑰念珠`,
  `Auspex = 鳥卜儀`, `Teleportarium = 傳送室`, `Rhino = 犀牛運兵車`,
  and `Land Raider = 蘭德掠襲者`.
- Eldar/Tyranid cleanup: `Warp Spider = 躍遷蛛`, `Wraithbone = 靈骨`,
  `Wraithguard = 幽冥守衛`, `Tyranid Warrior = 泰倫武士`,
  `Venom Brood = 毒液孵群`, `Fusion Gun = 熱熔槍`,
  `Fusion Blaster = 熱熔爆破槍`, and `Phoenix Lord Feugan =
  鳳凰領主弗甘`.
- Ork/Chaos/Guard cleanup: `Kommando Nob = 特戰老大`, Deffgun names use
  `噠咔死槍` / `光束死槍`, `Looted Tank = 掠奪坦克`, `Blastmaster =
  爆裂大師`, `Cadian = 卡迪安`, `Kasrkin = 卡斯金`, `Heavy Weapons Team =
  重型武器小隊`, `Vox Operator = 通訊兵`, and several Thaddeus/Eliphas/Tharp
  name consistency fixes.
- Mainland-style UI wording cleanup: `戰鎚` -> `戰錘`, video/audio wording
  normalized to `視頻` / `音頻`, and xenos wording normalized from `異形` to
  `異族` where appropriate.

Validation: Retribution output rebuilt successfully and remained 71720 lines.
Encoding scan found no U+FFFD. Expanded old/recent-problem scan returned 0 hits
for the current target list. `???` appears only in the original English/TChinese
placeholder rows 511755 and 607755. Same-as-English ASCII rows were limited to
variables, UI tokens, Ping strings, URLs, version/clock values, copyright/system
text, and similar technical placeholders. `git diff --check` reported no
whitespace errors.

### 2026-05-22 00:26-00:40 JST

Main-chat resumed Retribution-only translation and QA pass. DOW2 / Chaos Rising
was not actively targeted because the user has already cleared DOW2 in-game.
The pass continued the interrupted main-chat workflow, edited
`scripts/ucs_pipeline.py`, and rebuilt only:

```text
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Scope covered:
- Grenade and missile terminology cleanup: `穿甲導彈` -> `破甲導彈`,
  `盲光手雷` / `致盲榴彈` -> `致盲手雷`, `煙霧榴彈` -> `煙霧手雷`,
  and `震撼彈` -> `震撼手雷`.
- Equipment cleanup: `衝鋒炮` -> `突擊炮`, `機炮` / `自動加農炮` ->
  `自動炮`, `等級鍊劍` -> `等級鏈鋸劍`, Flamer descriptions now explicitly
  use `火焰噴射器`, and Executioner unit/name rows use `處刑者`.
- Ork cleanup: `Shoota Boyz` visible names now use `突突小子`, `Stormboyz`
  use `風暴小子`, Gretchin/Grot contexts use `屁精`, and Snotling contexts were
  kept distinct as `鼻涕精`.
- Space Marine veteran cleanup: Sternguard visible names were unified to
  `堅衛老兵`.

Validation: Retribution output rebuilt successfully and remained 71720 lines.
Encoding scan found no U+FFFD. Expanded old/recent-problem scan returned 0 hits
for the current target list, including the newly cleaned missile, grenade,
Autocannon, Assault Cannon, Sternguard, Shoota Boyz, and duplicate-Flamer
patterns. Same-as-English non-placeholder candidates were limited to technical
tokens, UI IDs, URLs, Ping strings, version/clock values, and similar internal
strings.

### 2026-05-21 02:09-02:49 JST

Main-chat Retribution-only translation and QA pass. Per user direction, DOW2 /
Chaos Rising was not actively translated in this run. Edits were made in
`scripts/ucs_pipeline.py`, and only the Retribution UCS was rebuilt with
`--game retribution`.

Scope covered:
- UI/system cleanup for residual English and placeholder-like strings: no-key
  text, command/help strings, Steam/authentication messages, CPU/GPU graphics
  requirement text, Direct2Drive/Steam store labels, and camera/control tips.
- Ork terminology cleanup: Wartrukk = `戰爭卡車`, Battlewagon = `戰鬥貨車`,
  Shoota = `突突槍`, Big Shoota = `重型突突槍`, Twin-linked Shoota =
  `雙聯突突槍`, Kustom Shoota = `特製突突槍`, Loota = `劫掠小子`, and Dakka
  Deffgun = `噠咔死槍`.
- Eldar / Tau / Necron cleanup: Autarch = `大司戰`, Brightlance = `光矛`,
  Shuriken Catapult = `星鏢彈射器`, Fire Warrior Squad = `火戰士小隊`, Greater
  Good = `上上善道`, XV8 Crisis Battlesuit = `XV8 危機戰鬥服`, XV88 Broadside
  Battle Suit = `XV88 寬舷戰鬥服`, Shas'O = `沙斯'O`, and Monolith = `方尖碑`.
- Tyranid / Imperial / Space Marine cleanup: Carnifex = `卡尼菲克斯`,
  Carnifex Alpha = `卡尼菲克斯首領`, Hormagaunt = `刀蟲`, Termagant = `槍蟲`,
  Mycetic Spore = `菌囊孢子`, Barbed Strangler = `倒刺絞殺炮`, Storm Trooper =
  `暴風突擊隊`, Assault Marine = `突擊星際戰士`, Tactical Marine =
  `戰術星際戰士`, and Force Commander = `指揮官`.
- Vehicle/Chaos cleanup: Land Raider = `蘭德掠襲者`, Land Raider Redeemer =
  `蘭德掠襲者救贖者`, Basilisk = `蛇怪自行火炮`, Basilisk Creeping Barrage =
  `蛇怪徐進彈幕`, Demolisher Cannon = `拆毀者炮`, Chaos Sorcerer =
  `混沌巫師`, Plague Champion = `瘟疫冠軍`, and Warmaster = `戰帥`.
- Lore equipment cleanup: restored key proper nouns in long descriptions,
  including Aquila Ignis as `烈焰天鷹`, Goge Vandire as `戈吉·范迪爾`,
  Strike Cruiser Retribution as `打擊巡洋艦「懲戒」`, and Legion of the Damned
  as `受詛軍團`.
- Traitor legion cleanup: fixed standalone `Death Guard` to `死亡守衛` by exact
  ID so it does not collide with `Deathwatch = 死亡守望`.
- Champion cleanup: normalized old `武聖` forms to `冠軍`, including Chaos,
  Eldar, Khorne, Tzeentch, Night Lords, and Plague Marine Champion contexts.
  `Plague Marine`-related visible names now use `瘟疫星際戰士` rather than
  old `疫病戰士`.

Rule additions for future work: keep WAAAGH untranslated as `WAAAGH`; do not
revert `Razorback = 剃刀背運兵車`; use `卡尼菲克斯首領` rather than
`卡尼菲克斯阿爾法`; use `戰帥阿巴頓` for `Warmaster Abaddon`; avoid old
forms such as `風暴兵`, `亮矛`, `掠奪小子`, `劊子獸`, `賀瑪岡特`,
`特瑪岡特`, `石化蜥蜴`, `混沌術士`, and `疫病冠軍`.

Validation after the final rebuild: Retribution output remained 71720 lines.
Expanded old-problem scan returned 0 hits for the current legacy term list,
including `神靈族`, `渾沌`, `歐克`, `毆克`, `太空陸戰隊`, `帝國衛隊`,
`電漿`, `飛彈`, `暗黑色軍團`, `哇啊啊`, `亮矛`, `星際突擊兵`, `掠奪小子`,
`風暴兵`, `劊子獸`, `賀瑪岡特`, `特瑪岡特`, and `菌絲孢子`. Same-as-English
ASCII equality candidates were down to technical placeholders, commands, URLs,
copyright/legal strings, Tau sept names, and internal UI tokens.

### 2026-05-21 01:29-02:09 JST

Main-chat Retribution-only pass. DOW2 / Chaos Rising was not actively targeted
because the user has already cleared DOW2 in-game. The pass edited
`scripts/ucs_pipeline.py`, rebuilt Retribution output only, and wrote:

```text
I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs
```

Scope covered: Chaos Shrine / Predator tutorial consistency, Demolisher Cannon,
Abaddon / Dark Gods / Khorne / Slaanesh lines, shortened Last Stand and wargear
lore descriptions, Tyranid / Eldar / Imperial Guard wargear descriptions,
Kyras / Diomedes / Galan ending text, Thousand Sons / Ahriman references, force
staff terminology, Doombolt terminology, Ork Kommando / Nob / Big Shoota text,
Ranger Long Rifle, Deathspinner, Venom Cannon, Exarch upgrades, and several
obvious old-TChinese omissions where long English descriptions had been reduced
to short summaries.

Rule additions for future work: use `混沌神龕` for Chaos Shrine but keep
`混沌聖殿` for Chaos Temple; use `掠食者殲滅者` for Predator Annihilator and
`掠食者毀滅者` for Predator Destructor; use `拆毀者炮` for Demolisher Cannon;
use `力場法杖` for Force Staff; use `末日閃電` for Doombolt; use `千子` for
Thousand Sons and `阿里曼` for Ahriman. Preserve `WAAAGH` rather than translating
it phonetically.

Validation during the run: Retribution UCS rebuilt successfully after each
batch. Stable line count remained 71720. Old-problem scan returned 0 hits for
the expanded target list, including Thousand Sons / force staff / Doombolt
cleanup terms. Residual same-as-English/ascii equality scan stayed at 134 and
consisted of placeholders, UI tokens, URLs, copyright/legal text, Tau sept names,
and command strings. Encoding scan found no U+FFFD and only the known original
`??` placeholder IDs 511755 and 607755.

### 2026-05-21 01:09-01:27 JST

Main chat Retribution-only translation and QA pass. Per user direction, DOW2 /
Chaos Rising was not actively targeted. Edits were made in
`scripts/ucs_pipeline.py`, and Retribution output was rebuilt repeatedly with
`--game retribution`.

Scope covered:
- Last Stand Tau / Necron / Ork hero tooltip polish: Crisis battlesuit jump and
  shield wording, markerlight / Sky Ray / seeker missile text, Overlord
  Staff of Light / Warscythe / Cryptek / C'tan lore, and WAAAGH / Boss Aura
  passive descriptions.
- Imperial Guard / Lord General cleanup: Guardsmen names normalized to
  `星界軍士兵`, Vox Caster to `通訊員`, Vanquisher turret/tank to `殲滅者`,
  Executioner to `處刑者`, Tarantula Turret to `狼蛛炮塔`, and Storm Trooper /
  Ogryn support text polished.
- Ability wording cleanup: `單個目標` -> `單一目標`, `受到更多傷害` ->
  `受到更高傷害`, `常時啟用` -> `常駐生效`, and several direct-translation
  phrases around knockback, stun, aura, and range-damage effects were smoothed.
- Known Razorback wording remains `剃刀背運兵車`; do not change it back to
  `疣豬` / `豪豬` unless the user explicitly chooses a different convention.

Rule additions for future work: use `殲滅者` for Vanquisher, `處刑者` for
Executioner, `狼蛛炮塔` for Tarantula Turret, `墓穴技師` for Cryptek,
`光杖` for Staff of Light, `戰鐮` for Warscythe, `星神` for C'tan,
`太空死靈` for Necron, and `懼亡者` for Necrontyr. Keep active passes focused
on Retribution unless the user asks for DOW2 again.

Validation during this run: Retribution output rebuilt successfully and remained
71720 lines. Legacy old-problem scan returned 0 hits for the current expanded
term list. Encoding scan found no U+FFFD and only the two known original `???`
placeholder rows at IDs 511755 and 607755. Same-as-English ASCII equality count
remained 134, consisting of legal/copyright strings, commands, internal codes,
Tau sept names, and other technical strings.

### 2026-05-21 00:37-01:08 JST

Main chat Retribution-only translation pass. Per user direction, DOW2 / Chaos
Rising was not actively targeted. Edits were made in `scripts/ucs_pipeline.py`
and Retribution output was rebuilt repeatedly with `--game retribution`.

Scope covered:
- Last Stand / Retribution UI and unit text: Intel role text, Lord General /
  Ogryn / Storm Trooper wording, Bloodletter Warp Shift duplicates, Tau drone
  and Crisis battlesuit wording, and role/order descriptions.
- Chaos terminology cleanup: `混沌神殿` -> `混沌神龕`, `瘟疫之神` -> `納垢`,
  `瘟疫戰士` -> `瘟疫星際戰士`, `Bloodcrusher` -> `碾血者`, and
  Tzeentch shrine / bolt wording.
- Ork cleanup: `Nob Leader` is now normalized as `老大`, `Stormboyz` as
  `風暴小子`, `Lootas` as `掠奪小子`, and Mekboy / Wartrukk / Brightlance
  support text was polished.
- Equipment and lore cleanup: `Brightlance` -> `光矛`, `D-cannon` -> `D-炮`,
  `Lord General` -> `星界軍將軍`, `Neroth` -> `奈若斯`, `Meridian` ->
  `梅里迪安`, and several Abaddon / Kyras / Eliphas lines were smoothed.
- Mechanical cleanup after `近身` -> `近戰`: fixed generated duplicates such
  as `近戰戰武器`, `近戰戰打擊`, `近戰戰中`, and `近戰戰防護`.

Rule additions for future work: keep active passes focused on Retribution unless
the user asks for DOW2 again; use `混沌神龕` for Chaos Shrine/Temple upgrade UI,
`老大` for Nob Leader, `星界軍將軍` for Lord General, `光矛` for Brightlance,
`D-炮` for D-cannon, `奈若斯` for Neroth, and `梅里迪安` for Meridian.

Validation after the final rebuild: Retribution output remained 71720 lines.
Expanded old-problem scan returned 0 hits, including legacy terms and this
run's new cleanup targets (`混沌神殿`, `瘟疫之神`, `老大頭目`, `光束長槍`,
`D 型炮`, `內羅斯`, `泰論`, `帝國將軍`, and generated `近戰戰...`
duplicates). Encoding scan found no U+FFFD, no `WAAAGH?`, and only the two
known original `???` placeholder rows at IDs 511755 and 607755. Same-as-English
ASCII equality count remained 134, consisting of UI tokens, commands, URLs,
copyright/legal text, Tau sept names, and similar technical strings.

### 2026-05-19 23:25-00:05 JST

Main chat Retribution-only translation pass started at 23:25:21 JST. Per user
direction, DOW2 / Chaos Rising was not actively translated in this run. Edits
were made in `scripts/ucs_pipeline.py` final replacement tables and ID-level
overrides, and only the Retribution UCS was rebuilt with `--game retribution`.

Major fixes in this run:
- Ork cleanup: normalized Nob Leader as `老大頭目`, Kommando as `特戰小子`,
  Kommando Nob as `特戰老大`, Shoota/Slugga loading-tip language, Big Shoota
  / Dakka text, and Storm Trooper false positives caused by `突擊隊` cleanup.
- Imperial / Space Marine cleanup: unified Sentinel as `哨衛機甲`, cleaned
  Guardsman residual forms to `星界軍士兵`, fixed Assault Terminators as
  `突擊終結者`, and kept `Scout = 偵察兵` in UI/loading tips.
- Eldar cleanup: unified Wraithguard as `幽冥衛士`, Warlock as `術士`,
  Mind War as `靈能戰`, Last Stand UI as `最後一戰`, and residual Exarch
  mistranslations from `主教` / `軍神` to `司戰`.
- Tyranid cleanup: unified `Tyranid Warrior = 泰倫武士`, `Hive Fleet =
  蟲巢艦隊`, `Pheromone = 信息素`, `Mycetic Spore = 菌囊孢子`, and
  Hormagaunt / Termagant loading-tip text as `刀蟲` / `槍蟲`.
- Chaos / campaign cleanup: normalized `Eliphas = 艾里法斯`,
  `Ulkair = 烏凱爾`, `Selenon = 塞勒農`, and `The Ice Works = 冰工廠`.
- Mainland-style UI/prose cleanup: corrected `最後戰役`, `高手信息`,
  `補給在線`, `戰在線`, and several awkward Last Stand attribute-scaling
  descriptions.

Validation during the run: Retribution UCS rebuilt successfully after each
batch and retained the stable 71720 line count. Targeted scans after each batch
returned 0 hits for the newly fixed bad forms, including `最後戰役`,
`心靈戰`, `艾達靈族`, `衝鋒槍小子`, `特馬根`, `賀馬根`,
`女妖主教`, `嚎叫女妖軍神`, `費洛蒙`, and `孢囊孢子`.

### 2026-05-19 00:24-01:04 JST

Main chat Retribution-only translation pass started at 00:24:52 JST. Per user
direction, DOW2 / Chaos Rising was not actively translated in this run. Edits
were made in `scripts/ucs_pipeline.py` final replacement tables, and only the
Retribution UCS was rebuilt with `--game retribution`.

Major fixes in this run:
- Ork cleanup: preserved `WAAAGH` as a faction concept, normalized
  `Warboss = 戰爭頭目`, and cleaned Shoota Boyz, Kommando, Wartrukk, Looted
  Tank, Deff Dread, and related vehicle/unit terms.
- Eldar cleanup: fixed Khaine/Avatar/Exarch terms, including
  `Avatar of Khaine = 凱恩戰神分身`, `Exarch = 司戰`, `Fire Prism =
  火稜鏡`, `Ulthwé = 烏斯維`, `Biel-Tan = 貝爾坦`, `Young King = 幼王`,
  and residual `蓋恩`/`神官` forms.
- Tyranid cleanup: normalized `Ravener = 掘蟒`, `Ripper = 撕裂蟲`,
  `Zoanthrope = 靈能蟲`, `Swarmlord = 蟲群之主`, and
  `Lictor Alpha = 利卡特阿爾法`.
- Chaos / Black Legion cleanup: fixed Bloodcrusher, gas grenade, plague lord
  terms, checked Abaddon dialogue, and unified `Araghast the Pillager` as
  `掠奪者亞拉哈斯特`.
- Mainland-style UI/prose cleanup: kept `文件`, `在線`, `網絡`, `鼠標光標`,
  `治療`, `附近`, `召喚`, and similar mainland phrasing in Traditional Chinese.
- Context and glossary rules were synchronized for Exarch, Avatar of Khaine,
  Fire Prism, Ravener, Zoanthrope, Deff Dread, Wartrukk, Bloodcrusher, and
  Araghast.

Validation during the run: Retribution UCS rebuilt successfully after each
batch and retained the stable 71720 line count. Expanded old-problem scan
returned 0 actionable hits for the tracked legacy terms and bad forms,
including `渾沌`, `神靈族`, `歐克`, `電漿`, `飛彈`, `哇啊啊`,
`Waaagh`, `蓋恩`, `神官擁有`, `吞噬蟲`, `死無畏`, `阿拉哈斯特`,
and `亞拉加斯`. Same-as-English ASCII scan after ID 9000000 reported 110
rows, all appearing to be variables, sound tags, hardware values, short UI
tokens, copyright/legal text, Tau sept names, or intentional `WAAAGH` rather
than normal untranslated prose.

### 2026-05-18 23:41-00:16 JST

Main chat Retribution-only translation pass started at 23:41:08 JST. Per user
direction, DOW2 / Chaos Rising was not actively translated in this run. Edits
were made in `scripts/ucs_pipeline.py` final replacement tables, and
Retribution UCS was rebuilt after each small batch with `--game retribution`.

Major fixes in this run:
- Retribution Chaos/Ork/Last Stand tooltips: Warboss passive/unlock text,
  Chaos Sorcerer / Subjugate / Doppelganger / Bloodletter abilities, corruption
  global abilities, Tarkus/Avitus corrupted abilities, Khorne slogans, and
  Tyrant Guard taunt descriptions.
- Corrected several real mistranslations: the corruption revive-all-sergeants
  global ability, remote explosive ally-sacrifice text, Daemonic Doppelganger
  as `替身`, Warboss `Scallywags` as `叛變雜碎`, and multiple single-target /
  controlled-singularity / psychic-dome descriptions.
- Polished wargear and lore lines around Blood Ravens relics, Astral Claws,
  Black Legion, Abaddon, Typhon / Judgment of Carrion background, skull/Khorne
  wording (`血祭血神！顱獻顱座！`), and heavy-infantry descriptions.
- Polished Eldar / Lord General / Tau / Last Stand ability text, including
  Autarch / Swooping Hawk wings, shield and marker drones, flare, Holy Pyre,
  D-Cannon singularity, and anti-armor missile descriptions.
- Final cleanup after validation: normalized visible `Ability Unlock -` /
  `解鎖技能 -` strings to `能力解鎖：`, changed residual hand-to-hand wording
  to melee wording, aligned remaining Daemonic Doppelganger strings to
  `惡魔替身` / `替身`, and fixed several small UI phrases around upgrade unlocks,
  minion traits, `黑暗靈能`, and `30 秒`.
- Rule files were synchronized with current user-approved terminology:
  `glossary/STYLE_GUIDE.md` and `glossary/mainland_40k_tw.tsv` now explicitly
  prefer `星界軍`, `無畏機甲`, `戰爭頭目`, `WAAAGH`, and
  `Daemonic Doppelganger = 惡魔替身`.
- Post-push sweep corrected several Retribution corruption/redemption score
  notices, including restoring the `%1REDEMPTION%` variable for redemption rows
  and rewriting `from wargear / for not deploying / expiring` labels into
  readable Traditional Chinese.

Validation during the run: Retribution output rebuilt successfully and retained
the stable 71720 line count. Expanded old-problem scan returned 0 hits for the
tracked legacy terms and bad forms including `渾沌`, `神靈族`, `歐克`, `電漿`,
`飛彈`, `哇啊`, `嘲弄`, `飯桶`, `兇靈`, `Ability Unlock`, `Doppelganger`,
`惡魔分身`, `黑暗魔法`, and `卅秒`. Encoding scan found no U+FFFD, no
`WAAAGH?`, no lowercase `Waaagh`, no generic `哇啊啊`, and only the two
original `???` placeholder rows at IDs 511755 and 607755. Remaining
same-as-English ASCII rows after ID 9000000 counted 99 and are placeholders,
sound tags, legal text, chat commands, URLs, Tau sept names, or WAAAGH rather
than normal visible prose. DOW2 / Chaos Rising output was not rebuilt or
actively translated in this run.

### 2026-05-18 00:44-01:03 JST

Main chat 20-minute translation pass started at 00:44:32 JST and continued in
`scripts/ucs_pipeline.py` final override rules, with UCS rebuilds after each
small batch. The run focused on visible tutorial text, ability descriptions,
unit and vehicle terminology, and old mechanical `給予` / `得到` wording.

Major fixes in this run:
- DOW2 and Retribution tutorial cleanup: highlighted-area prompts, Force
  Commander resilience, stimulant-pack guidance, combat training unlocks,
  Cyrus ammunition unlocks, Thaddeus reckless-state text, Jonah staff/Avenger
  unlocks, and multiple ability-unlocked descriptions.
- Ork and Mek cleanup: `Shoota Boyz = 獸人槍小子`; `Mek/Mekboy = 技霸/技霸小子`;
  Big Mek wargear and force-field descriptions; preserved `WAAAGH!` as the
  Ork war cry/concept.
- Tyranid cleanup: `Hormagaunt = 刀蟲`, `Termagant = 槍蟲`, and `Hive = 蟲巢`;
  removed remaining old `角蟲`/`蟲王` output hits.
- Vehicle cleanup: fixed a DOW2 `Land Raider` line that had been mistranslated
  as `掠食者坦克`; unified `Land Raider = 蘭德襲擊者` and `Land Raider Redeemer =
  蘭德襲擊者救贖者`; fixed a `Razorback` combat line that had been mistranslated
  as `犀牛運兵車`.
- Wargear/lore cleanup: `Artificer Power Armor = 精工動力甲`, daemon shield,
  Dreadnought and Land Raider status lines, smoke grenade building-eviction
  text, and several Chaos Rising corruption/ability lines.

Validation during the run: both UCS outputs rebuilt successfully and kept the
stable line counts, dow2 50695 and retribution 71720. Old problem term scan,
including `角蟲`, `蟲王`, `獸人槍槍小子`, and `蘭德掠襲者`, returned 0 hits.
Encoding scan showed only the original `???` placeholder IDs 511755 and 607755
in both outputs. `git diff --check` reported only CRLF normalization warnings.

### 2026-05-18 00:14-00:42 JST

Main chat translation run started at 00:14:23 JST. The run focused on a
script-level final override pass in `scripts/ucs_pipeline.py`, followed by
standard all-game UCS rebuilds. This batch prioritized visible gameplay text,
DOW2 lines where Retribution already had better wording for the same English
ID, and obvious old mistranslations.

Major fixes in this run:
- DOW2 tutorial/UI cleanup: unit selection, camera focus, attack/move orders,
  rally points, supply crates, power nodes, resource descriptions, fall-back
  guidance, Zeal/global ability text, equipment/accessory explanations, and
  profile recovery prompts.
- DOW2 campaign cleanup: early Ork tutorial lines, Argus/Calderis/Typhon
  Hive Fleet exposition, Angel Forge and final Hive Ship objective text,
  Zoanthrope/Hive Mind descriptions, Avitus/Thaddeus/Cyrus ability guidance,
  and several secure-stratagem messages.
- Wargear/lore cleanup across both outputs: Assault Cannon lore, plasma pistol
  and Dark Angels/Caliban references, Imperial Fists/Salamanders/Space Wolves
  relic text, Techmarine Isaak Jordanos, Kronus/Imperial Guard background, and
  several Blood Ravens relic descriptions.
- Chaos Rising cleanup: Judgment of Carrion/Galan expedition summaries,
  Great One/Kyras lines, vox-cloak text, Space Hulk boarding lines, holy/unholy
  fury descriptions, warp tome descriptions, and daemon/Eliphas dialogue.
- Retribution cleanup: Chaos Sorcerer abilities, Lord General/Storm Trooper
  ability text, Eldar/Exarch ability descriptions, Imperial Guard campaign
  dialogue, Ork voice lines, and late profile/stat recovery prompts.
- Terminology additions: `Swarmlord = 蟲群之主`; `Servitor = 機僕` only for
  mechanic construct contexts; `Caliban = 卡利班`; `Vulkan = 伏爾甘`.

Validation during the run: both UCS outputs rebuilt successfully after each
batch. Stable line counts remained dow2 50695 and retribution 71720. Old-term
scan for the known problem list returned 0 hits. Encoding scan found no
replacement-character corruption and only the original `???` placeholder IDs
511755 and 607755 in both outputs. Final git commit/push was performed from
the main chat after validation.

### 2026-05-17 22:58-23:38 JST

Main chat 40-minute active translation pass continued in
`scripts/ucs_pipeline.py` and rebuilt both UCS outputs after each small batch.
Scope: Blood Angels/Black Rage/Crimson Fists/Deathwing/Iron Warriors naming,
Army Painter and DLC copy, Mekboy/Big Mek wording, Plasma Gun entries, remaining
Retribution Last Stand residual-English equipment/trait strings, Thule/Angelos/
Kronus campaign wording, DOW2 Thule cure campaign alignment, and a large DOW2
Tyranid cleanup pass.

Important terminology stabilized this run: `Tyranids = 泰倫蟲族`, `Synapse =
突觸`, `Bio-toxin = 生物毒素`, `Biomorph = 生體變異`, `Hive Fleet Leviathan =
利維坦蟲巢艦隊`, `Hive Fleet Behemoth = 貝希摩斯蟲巢艦隊`, and branch fleets as
`分支艦隊`. Kept Ordo Xenos / generic xenos contexts as `異形` or `異族`, so
`異形` was not globally replaced.

Final small pass also aligned `Tarsis Ultra = 塔西斯·奧特拉`, `Ultramar =
奧特拉瑪`, Behemoth tendril names, and `Barding of Ultramar = 奧特拉瑪甲胄`.

Validation after final rebuild: dow2 50695 lines, retribution 71720 lines.
Old problem term scan returned 0 hits, Tyranid/Synapse/Biomorph English-residue
scan returned 0 hits, and WAAAGH bad-form scan returned 0 hits. Encoding scan
found no replacement-character hits; the only `???` lines remain the existing
placeholder IDs 511755 and 607755 in both outputs.

### 2026-05-17 22:17-22:57 JST

Main chat 40-minute active translation pass continued in
`scripts/ucs_pipeline.py` and rebuilt both UCS outputs after each small batch.
Scope: Deathwatch/Death Guard disambiguation, Power Generator and Tarantula
turret wording, Force Commander vs Eldar Exarch cleanup, Horus Heresy/Trythos
/ Lord of Flies lore fixes, Chapter armory and Machine God terminology, thunder
hammer/storm shield standardization, Isador Akios and Ruinous Powers fixes,
Superior/Relic weapon quality names, Blind Grenade wording, Eldar insult and
installer wizard fixes, Guardsman/Guardsmen -> 星界軍士兵 context cleanup, `炮`
glyph unification, Chapter -> 戰團 fixes, Blood Ravens Company numbering, and
第85文多蘭星界軍團 / 能量力場 / 力場發生器 terminology.

Important additions for future rules: keep `雷霆錘` and `風暴盾`; translate
`Superior` equipment as `精良`, `Relic` equipment as `遺物`, `Blind Grenade` as
`致盲手雷`, `Chapter` as `戰團`, `Company` as `連` in Space Marine organization,
and `Guardsman/Guardsmen` as `星界軍士兵` when referring to Imperial Guard
personnel. Preserve `Planetary Defense Force` as `行星防衛部隊`.

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

### 2026-05-17 23:36 JST

Main chat translation run started at 23:36:35 JST and continued until shortly
after 00:12 JST on 2026-05-18, with final validation and commit/push still to
follow. Scope was a long-tail consistency and quality pass across both DOW2 and
Retribution outputs, implemented in `scripts/ucs_pipeline.py` and rebuilt with
the standard `ucs_pipeline.py --process-root I:\translate_process build --game
all --fill-missing english` command.

Major fixes in this run:
- UI/tutorial cleanup: camera panning, mouse selection, limited-use ability
  counters, supply drops, wargear pickup, donated wargear, first poison point,
  and Thule/Dreadnought recovery text.
- Placeholder cleanup: all `Grenade Extra Text goes here` derivatives now
  normalize to `手雷額外文字在此`.
- Raven Guard lore cleanup: standardize Raven Guard as `鴉衛`, Kayvaan Shrike as
  `凱萬·史萊克`, Squiggoth as `史奎格巨獸`, and clean several weapon lore
  descriptions around Polyphemus, Bloodtide, Buckley Purgation, and Haugaard.
- Chaos Rising/Kyras/Abaddon cleanup: retranslated obvious bad lines around
  Great One/Kyras, Chapter Master and Chief Librarian text, Aurelia/Judgment of
  Carrion references, Eliphas/Kyras ending text, and several Retribution chaos
  campaign lines involving Abaddon, Kyras, Typhon, the Ordo Malleus, and
  daemonhood.
- Ultramarines and background lore cleanup: standardize `奧雷利亞`, `阿格斯`,
  `基里曼`, `提古里烏斯`, `托里亞斯·泰利昂`, `阿斯提亞納克斯`,
  `洛恩 V`, `瓦努斯牧師`, `技術軍士`, and related wargear/lore strings.
- Purity terminology cleanup: `Purity Seal` is now `純潔印記` instead of
  `貞潔封印` / `貞潔之契`; `Pure Trait` / purity system text now uses `純潔`.

Rule additions for future work: keep `screen` as `螢幕` in Traditional Chinese
UI text, not `屏幕`; use `純潔印記` for `Purity Seal`; use `鴉衛` for Raven
Guard; use `技術軍士` for Techmarine; use `凱萬·史萊克` for Kayvaan Shrike;
use `史奎格巨獸` for Squiggoth; use `奧雷利亞` for Aurelia and `阿格斯` for
Argus.

Validation during the run: both UCS outputs rebuilt successfully; line counts
remained stable at dow2 50695 and retribution 71720. Encoding scan showed only
the original `???` placeholder IDs 511755 and 607755 in both games. Old-term
scan returned only a false positive where `嚎叫女妖最適合` contains the old
substring `女妖最適合`; no actionable old-term hit remained from this run's
target list. Same-as-English/ascii equality scan mostly reported placeholders,
format strings, UI tokens, `Ping`, URLs, and other non-localized technical
tokens.

### 2026-05-18 22:56-23:36 JST

Main-chat pass switched to Retribution-only active translation after user
confirmed DOW2 / Chaos Rising had been cleared in-game. DOW2 should no longer be
actively targeted unless the user asks. The pass edited
`scripts/ucs_pipeline.py`, rebuilt Retribution only, and wrote the generated UCS
to `I:\translate_process\translation_project\output\retribution\Locale\TChinese\DOW2.ucs`.

Scope covered: Last Stand ability and unlock descriptions, Lord General /
Ogryn / Commissar Lord Bernn text, Ork Spookums / Lootas / Kommandos / More
Dakka wording, Tyranid Hive Lord and Zoanthrope-adjacent cleanup, Tau drone and
Crisis battlesuit lines, Steam / lobby UI wording, Kayleth draw-fire fixes,
Noise Marine / Blastmaster wording, Warp Spider cleanup, and several awkward
Chaos Rising / Ork wargear descriptions still visible in Retribution output.
Rule updates: `Dakka = 噠咔`; keep future active passes focused on Retribution.

Validation after rebuild: Retribution output remained 71720 lines. Expanded
old-problem scan returned 0 hits, including `神靈族`, `渾沌`, `歐克`,
`毆克`, `太空陸戰隊`, `電漿`, `飛彈`, `哇啊`, `傳送蜘蛛`,
`發出火焰`, `放血鬼鬼王`, `搭嘎嘎`, `覆覆`, and related typo patterns.
Encoding scan found no U+FFFD, no `WAAAGH?`, no lowercase `Waaagh`, and only the
two original `???` placeholder rows at IDs 511755 and 607755.

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
