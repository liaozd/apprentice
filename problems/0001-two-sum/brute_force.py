"""1. 两数之和 — 解法一:暴力枚举

思路:
    双重循环枚举所有数对 (i, j),i < j,找到和为 target 的一对即返回。

复杂度:
    时间 O(n²):枚举 n(n-1)/2 对
    空间 O(1):不使用额外空间
"""


def solve(nums: list[int], target: int) -> list[int]:
    # TODO(练习):实现暴力枚举。提示:
    #   1. 外层 i 从 0 到 n-2,内层 j 从 i+1 到 n-1
    #   2. nums[i] + nums[j] == target 时返回 [i, j]
    #   3. 题目保证有解,找不到可以 raise 或返回空列表

