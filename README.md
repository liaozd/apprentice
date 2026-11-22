# apprentice — 算法练习仓库

从零开始的 LeetCode 刷题练习。

每题一档:题目笔记(README)+ 多解法(每种解法一个文件)+ 参数化测试(`test_<编号>.py`)。
**解法由练习者自己实现** —— 脚手架只提供题意、思路提示、用例与测试闭环。

## 目录结构

```
apprentice/
├── problems/
│   └── 0200-number-of-islands/    # 第一题:README 笔记 + 3 个解法桩 + test_0200.py
├── templates/                     # 新题模板:problem_README.md / solution.py
│                                  # (测试文件无单独模板:复制 0200 的 test_0200.py 改)
├── notes/                         # 专题笔记,模式沉淀,复习用
│   └── graphs.md
├── pyproject.toml                 # pytest 配置 + dev 依赖
└── AGENTS.md                      # 代理工作约定
```

## 快速开始

```bash
uv sync                                          # 建 .venv 并安装 pytest(dev 组)
uv run pytest problems/0200-number-of-islands/ -v  # 跑第一题(初始全红 = 预期)
uv run pytest                                    # 跑全部
```

没有 uv 时:`python3 -m pip install pytest` 后直接 `pytest`。

## 练习闭环

1. 读题 → 在题目 README 记题意、列坑
2. 实现解法文件里的 `solve()` —— 先跑通一个解法,再逐个补齐其他解法
3. `uv run pytest problems/<题>/ -v` 变绿才算完成
4. 复盘写进 README,模式沉淀进 notes/ 对应专题
5. 状态改 ✅;隔段时间重刷时改 🔁

状态图例:⬜ 未开始 / 🔨 进行中 / ✅ 已通过 / 🔁 重刷

## 开新题

1. 新建 `problems/<4位编号>-<题名slug>/`
2. 复制模板:`templates/problem_README.md` → `README.md`;`templates/solution.py` → 每个解法文件
   (测试文件:复制 `problems/0200-number-of-islands/test_0200.py` 改 SOLVERS / CASES)
3. 把 LC 官方示例抄进 CASES;解法文件写成 docstring 思路 + TODO 桩
4. 新题初始测试全红是预期(解法还是 `NotImplementedError` 桩)

## 约定

- 每个解法文件暴露 `solve(...)` 统一入口
- 用例只写在 `test_<编号>.py`;解法可原地修改输入,测试按行拷贝保护
- 复习导向:README 复盘区和 notes/ 是半年后回看的核心资产
