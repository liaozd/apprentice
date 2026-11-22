"""200. 岛屿数量 — 解法一:DFS 染色(沉岛)

思路:
    遍历网格,每遇到一个 '1' 计数 +1,并立刻用 DFS 把与它相连的
    整块陆地全部改成 '0'(沉岛),保证每块独立岛屿只被计数一次。

复杂度:
    时间 O(m·n) — 每个格子至多被访问一次
    空间 O(m·n) — 最坏情况(全陆地)递归深度
"""


def solve(grid: list[list[str]]) -> int:
    # TODO(练习):实现 DFS 染色。提示:
    #   1. 双重循环找 '1' → count += 1 → 从每块新岛屿起点 DFS
    #   2. DFS 内:越界或 '0' 直接返回;先沉岛,再向四方向递归
    #   3. 大网格递归深度会超 Python 默认上限 1000:进阶用例(见
    #      test_0200.py 底部注释)需要显式栈,或临时 sys.setrecursionlimit
    raise NotImplementedError("实现 dfs.solve:遍历 + 染色")
