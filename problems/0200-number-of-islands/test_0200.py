"""200. 岛屿数量 — 用例

用例来源:LeetCode 官方示例 + 边界补充。
同一组用例跑本目录下所有解法;解法可以原地修改 grid,测试按行拷贝保护原始用例。
"""

import importlib.util
from pathlib import Path

import pytest

_DIR = Path(__file__).parent
# 不同题目录下会有同名解法文件(dfs.py / bfs.py……),pytest 默认导入模式下
# 裸 import 会在单进程内发生模块名冲突,因此按文件路径加载并加题目前缀。
_PREFIX = _DIR.name.replace("-", "_")


def _load(stem: str):
    spec = importlib.util.spec_from_file_location(f"{_PREFIX}_{stem}", _DIR / f"{stem}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVERS = {
    "dfs-染色": _load("dfs").solve,
    "bfs-队列": _load("bfs").solve,
    "并查集": _load("union_find").solve,
}

CASES = [
    # (grid, expected)
    # LC 官方示例 1:一块大连通陆地 → 1
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),
    # LC 官方示例 2:三块独立岛屿 → 3
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    ),
    # 边界:全水 → 0
    ([["0", "0"], ["0", "0"]], 0),
    # 边界:单格陆地 → 1
    ([["1"]], 1),
]

CASE_IDS = ["示例1", "示例2", "全水", "单格陆地"]


@pytest.mark.parametrize("solver", list(SOLVERS.values()), ids=list(SOLVERS.keys()))
@pytest.mark.parametrize("grid,expected", CASES, ids=CASE_IDS)
def test_num_islands(solver, grid, expected):
    # 解法可以原地沉岛;按行拷贝,保护原始用例
    board = [row[:] for row in grid]
    assert solver(board) == expected


# 进阶用例(实现后取消注释挑战):
#   300×300 全陆地大网格 — 递归 DFS 会 RecursionError(默认递归上限 1000),
#   需要:显式栈 DFS / BFS / 并查集,或临时 sys.setrecursionlimit
#
# def test_large_all_land():
#     grid = [["1"] * 300 for _ in range(300)]
#     assert SOLVERS["dfs-染色"]([row[:] for row in grid]) == 1
