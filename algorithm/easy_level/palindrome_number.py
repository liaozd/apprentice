#!/usr/bin/env python
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:

    输入: 121
    输出: true
    示例 2:

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution(object):
    def palindrome_number(self, num):
        if num < 0 or num == 10:
            return False
        reversed_half = 0
        while reversed_half < num:
            reversed_half = reversed_half * 10 + num % 10
            num = num // 10
        if reversed_half == num or reversed_half // 10 == num:
            return True
        return False


print(Solution().palindrome_number(10))
print(Solution().palindrome_number(123))
print(Solution().palindrome_number(12321))
print(Solution().palindrome_number(-123321))
