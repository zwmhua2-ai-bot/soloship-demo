# soloship-demo

SoloShip 自动化开发与 Draft PR 交付的**测试仓库**（Private）。不承载生产代码。

## 结构

```
src/todo.py          示例业务模块（TodoList）
tests/test_todo.py   标准库 unittest
ARCHITECTURE.md      仓库规则（Codex 必须读取）
AGENTS.md            自动化执行规则
```

## 测试

```powershell
py -3 -m unittest discover -s tests -v
```

只依赖 Python 标准库。

## 交付流程

任务经 SoloShip Bridge 在独立 worktree 中实现 → Bridge 独立跑测试 → 独立 Reviewer 审查 → 通过后由 Bridge 推送 `soloship/<task-id>` 分支并创建 **Draft PR**，等待人工验收。

不自动合并、不部署。
