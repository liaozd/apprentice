"""200. 岛屿数量 — 解法三:并查集(Union-Find)

思路:
    把每个 '1' 格子编号成 id = i * n + j,右方/下方相邻也是 '1' 就 union。
    有两种计数方式:
      a) 初始 count = 陆地数,每成功合并一次 count -= 1
      b) 最后遍历数不同根
    练习路径压缩 + 按秩合并。

复杂度:
    时间 O(m·n·α) — α 是反阿克曼函数,近似常数
    方式 b) 最后数根是 O(m·n)
    空间 O(m·n) — parent / rank 数组
"""

def solve(grid: list[list[str]]) -> int:
    # TODO(练习):实现并查集。提示:
    #   1. 编号 id = i * n + j,右方/下方相邻是 '1' → union
    #   2. 方式 a) 初始 count = 陆地数,成功合并一次 count -= 1
    #   3. find 路径压缩 + union 按秩合并
    raise NotImplementedError("实现 union_find.solve:相邻陆地合并")
