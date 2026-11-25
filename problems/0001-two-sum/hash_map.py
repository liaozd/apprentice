"""1. 两数之和 — 解法二:哈希表(一次遍历)

思路:
    遍历数组,对每个 nums[i] 计算需要的补数 target - nums[i],
    在哈希表(值 → 下标)中查找;查不到就把当前值存入哈希表。
    先查后存,天然保证不会用同一元素两次。

复杂度:
    时间 O(n):每个元素只访问一次,哈希查询均摊 O(1)
    空间 O(n):哈希表最多存 n 个元素
"""


def solve(nums: list[int], target: int) -> list[int]:
    # TODO(练习):实现哈希表法。提示:
    #   1. seen = {} 存 值 → 下标
    #   2. 遍历 i, v = nums[i]:need = target - v
    #   3. need in seen → 返回 [seen[need], i]
    #   4. 否则 seen[v] = i(先查后存,避免自配对)
