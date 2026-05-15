# Dawn of War II 繁中大陆译名修订工程

目标：保留游戏的 `TChinese` 语言槽和繁体中文字符，但采用中国大陆战锤 40,000 译名习惯修订 `Locale` 文本。

## 原则

- `DOW2.ucs` 的数字 ID 必须保持不变。
- 输出文件继续使用 UTF-16 编码。
- 文本保持繁体中文，不转换为简体。
- 术语优先服从 `glossary/mainland_40k_tw.tsv`。
- 英文 `DOW2.ucs` 作为完整 ID 基准，现有繁中只作为参考。
- 仓库不保存完整游戏文本、`.ucs` 输出文件、`.sga`、语音、贴图或其他游戏资源。

## 本地目录约定

仓库存放脚本和术语表，例如：

```text
I:\Github\translate_dow2
```

本地施工目录存放游戏文件副本和生成物，例如：

```text
I:\translate_process
```

施工目录需要包含：

```text
I:\translate_process\Dawn of War 2\Locale\English\DOW2.ucs
I:\translate_process\Dawn of War 2\Locale\TChinese\DOW2.ucs
I:\translate_process\Dawn of War II - Retribution\Locale\English\DOW2.ucs
I:\translate_process\Dawn of War II - Retribution\Locale\TChinese\DOW2.ucs
```

## 运行方式

从仓库目录运行，显式指定施工目录：

```powershell
python scripts\ucs_pipeline.py --process-root I:\translate_process report
python scripts\ucs_pipeline.py --process-root I:\translate_process term-report
python scripts\ucs_pipeline.py --process-root I:\translate_process export --game all
python scripts\ucs_pipeline.py --process-root I:\translate_process build --game all --fill-missing english
```

如果系统没有 `python` 命令，可以使用 Codex 运行时或你本机安装的 Python 可执行文件来调用同一个脚本。

生成物默认写入：

```text
I:\translate_process\translation_project\reports
I:\translate_process\translation_project\work
I:\translate_process\translation_project\output
```

## 基本流程

1. 运行覆盖率报告，确认英文与繁中 ID 差异。
2. 导出施工 TSV。
3. 在 TSV 的 `zh_new` 列填写或修订译文。
4. 生成新的 `DOW2.ucs` 到 `output/`。
5. 手动复制到对应游戏的 `Locale\TChinese\DOW2.ucs` 测试。

## 人工覆盖表

自动导出的 `work/*_translation.tsv` 可以反复重建。为了避免精修译文被覆盖，可以把人工修订条目放在：

```text
I:\translate_process\translation_project\work\manual_overrides.tsv
```

格式：

```text
game_key	id	zh_new	notes
all	920012	蠻荒獸人	同时作用于两个游戏
dow2	809016	獸人砲兵陣地	只作用于 DoW2
retribution	809016	獸人砲兵陣地	只作用于 Retribution
```

`game_key` 可填 `dow2`、`retribution` 或 `all`。构建时人工覆盖表优先级最高。
