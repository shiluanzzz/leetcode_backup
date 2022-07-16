#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
import itertools
from operator import le
from os import pread
# @lc code=start
class NumArray:

    def __init__(self, nums: list[int]):
        self.pre_sum=list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.pre_sum[right]
        else:
            return self.pre_sum[right]-self.pre_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

