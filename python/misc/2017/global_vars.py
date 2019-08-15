#!/usr/bin/env python

num = 100


def test1():
    global num
    num += 100


print(num)
test1()
print(num)

nums = [1, 2]


def test2():
    nums.append(33)


print(nums)
test2()
print(nums)