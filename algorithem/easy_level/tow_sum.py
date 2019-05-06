#!/usr/bin/env python
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
"""


class Solution(object):
    def two_sum(self, nums, target):
        maps = dict()
        for i, _num in enumerate(nums):
            subtracted = target - _num
            if _num in maps:
                return maps[_num], i
            else:
                maps[subtracted] = i
        return -1, -1


target = 9
nums = [2, 7, 11, 15]

print(Solution().two_sum(nums, target))
