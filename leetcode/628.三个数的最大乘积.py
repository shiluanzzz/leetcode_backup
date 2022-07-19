#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
import re


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        z,f=[],[]
        for i,v in enumerate(nums):
            if v>=0:
                z.append(v)
            else:
                f.append(v)
        if len(z)>=3:
            z.sort(reverse=True)
            return z[0]*z[1]*z[2]
        else:
            f.sort()
            if len(f)>=2:
                return z[0]*f[0]*f[1]
            else:
                return z[-1]*z[-2]*f[0]
# @lc code=end
# [1,2,3,4,5],[-1,-2,-3,-4,-5],[-1,-2,-3,4],[-1,2,3,5],[-3,-2,5,6]
