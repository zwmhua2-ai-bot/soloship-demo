# soloship-demo 架构

## 1. 定位

SoloShip P03 的隔离测试仓库，用于验证"自动开发 → 独立审查 → Draft PR"链路。

## 2. 目录与边界

- `src/`：业务代码，允许 Codex 修改。
- `tests/`：标准库 `unittest`，允许 Codex 修改。
- `ARCHITECTURE.md`、`AGENTS.md`、`README.md`、`.gitignore`：默认只读，除非任务明确授权。

## 3. 测试

```powershell
py -3 -m unittest discover -s tests -v
```

## 4. 约束

- 单任务改动上限 200 行（含测试）。
- 不新增第三方依赖。
- 不建远程分支、不推送、不提 PR：分支与 PR 由 SoloShip Bridge 统一处理。
