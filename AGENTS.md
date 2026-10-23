# AGENTS.md · soloship-demo

本文件是仓库级规则，自动化任务以本文件为准。

- 只用 Python 标准库。
- 改完运行 `py -3 -m unittest discover -s tests -v`。
- 只实现任务要求的最小改动，保持现有行为。
- 只修改 `src/` 与 `tests/`。
- 不建分支、不 push、不提 PR、不合并、不部署——这些由 Bridge 负责。
- 不修改 `ARCHITECTURE.md`、`AGENTS.md`、`.gitignore`，不碰 `.git/`。
- 不请求人工确认，直接完成任务并跑测试；结束用 5 行内说明改动与结果。
