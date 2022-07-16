#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
import functools
from turtle import Turtle
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def cmp(a,b):
            if len(a)==len(b):
                return a>b
            else:
                # 34>3>30
                if len(a)<len(b):
                    return not cmp(b,a)
                nb=b+"0"*(len(a)-len(b))
                if nb==a:
                    return False
                else:
                    return a>nb
        nums=[str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if cmp(nums[i],nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]
        print(nums)
        return "".join(nums[::-1])
# @lc code=end

print(Solution().largestNumber([3,30,34,5,9]))