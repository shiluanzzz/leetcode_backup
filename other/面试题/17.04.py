# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？

def solve(nums:list)->int:
    if len(nums) ==0: return 0
    nums.sort()
    if len(nums)-1 == nums[-1]: return nums[-1]+1
    return set([i for i in range(nums[-1])]).difference(set(nums)).pop()

def  solve2(nums):
    return sum(range(len(nums)+1))-sum(nums)
print(solve2([1,2,3,4]))