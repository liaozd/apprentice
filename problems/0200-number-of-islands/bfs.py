"""200. 岛屿数量 — 解法二:BFS(队列)

思路:
    同样是"遇到陆地就染色",但用 collections.deque 做层序扩展,
    没有递归深度限制。注意:入队时立刻标记,出队时再标记会重复入队。

复杂度:
    时间 O(m·n)
    空间 O(min(m,n)) — 队列里最多同时装下一圈边界格子
"""

from collections import deque


def solve(grid: list[list[str]]) -> int:
    # TODO(练习):实现 BFS。提示:
    #   1. 双重循环找 '1' → count += 1 → 标记并入队
    #   2. 出队 → 向四方向扩展:在界内、是 '1' → 标记、入队
    #   3. 标记时机是本题最常见 bug 来源
    raise NotImplementedError("实现 bfs.solve:队列层序扩展")
