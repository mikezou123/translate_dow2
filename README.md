# Dawn of War II 繁中大陆译名修订工程

目标：保留游戏的 `TChinese` 语言槽和繁体中文字符，但采用中国大陆战锤 40,000 译名习惯重译 `Locale` 文本。

## 原则

- `DOW2.ucs` 的数字 ID 必须保持不变。
- 输出文件继续使用 UTF-16 编码。
- 文本保持繁体中文，不转换为简体。
- 术语优先服从 `glossary/mainland_40k_tw.tsv`。
- 英文 `DOW2.ucs` 作为完整 ID 基准，现有繁中只作为参考。

## 目录

- `glossary/`：大陆译名习惯的繁体中文术语表。
- `scripts/`：解析、报告、导出、生成 `.ucs` 的脚本。
- `reports/`：覆盖率和风险报告。
- `work/`：按游戏导出的翻译施工 TSV。
- `output/`：生成后的 `DOW2.ucs`，确认后再手动复制回游戏目录测试。

## 基本流程

1. 运行覆盖率报告，确认英文与繁中 ID 差异。
2. 导出施工 TSV。
3. 在 TSV 的 `zh_new` 列填写或修订译文。
4. 生成新的 `DOW2.ucs` 到 `output/`。
5. 手动复制到对应游戏的 `Locale\TChinese\DOW2.ucs` 测试。

