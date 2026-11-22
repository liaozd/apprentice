# AGENTS.md

个人算法练习仓库(LeetCode,Python 3)。
**解法由用户自己写**。代理负责脚手架、用例、笔记整理、代码审查、思路讲解;除非用户明确要求,不要代写 `solve()`。

## 结构
- `problems/<4位编号>-<slug>/` — 每题一档:README(题意/思路表/坑/复盘)+ 解法文件 + `test_<编号>.py`
- `templates/` — 新题模板:problem_README.md / solution.py(测试文件参照 0200 的 test_0200.py)
- `notes/` — 专题模式笔记(graphs.md 等),复习导向
- `openspec/` — OpenSpec 工作流(需求/变更走 /opsx:* 技能)

## 命令
- `uv sync` — 建 .venv 装依赖(pytest 在 dev 组)
- `uv run pytest` — 跑全部;`uv run pytest problems/<题>/ -v` — 单题;新题初始全红是预期

## 关键约定
- 每个解法文件暴露 `solve(...)` 统一入口;一题多解分文件存放
- 用例只写在 `test_<编号>.py`;解法可原地修改输入,测试按行拷贝保护原始用例
- **同名模块坑**:各题目录下会有同名解法文件(都有 dfs.py 等),pytest 默认导入模式下
  裸 import 会单进程模块名冲突 → 统一用“按文件路径加载 + 题目前缀”的 `_load()`
  (参照 `problems/0200-number-of-islands/test_0200.py`),不要改成裸 import
- 目录名带连字符,不是 Python 包,没有跨目录 import
- 笔记/注释用中文;解法文件结构 = docstring(思路+复杂度)+ solve() + NotImplementedError 桩
- 新题按模板创建;编号 4 位补零(0200),测试文件名 `test_<编号>.py` 与目录编号一致

## 练习性质
- `solve()` 留给用户实现;代理可写用例、审码、讲解,除非明确要求代写
- 新题脚手架的解法文件 = docstring 提示 + TODO 桩 + NotImplementedError
