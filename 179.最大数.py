#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
from re import L


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def cmp(a,b):
            if len(a)==len(b):
                return a>b
            else:
                # 34>3>30
                t1=a+b
                t2=b+a
                return t1>t2
        nums=[str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if not cmp(nums[i],nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]
        if nums[0]=='0':return '0'
        return "".join(nums)
# @lc code=end

