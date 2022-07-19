#
# @lc app=leetcode.cn id=2293 lang=python3
#
# [2293] 极大极小游戏
#

# @lc code=start
import enum
from hashlib import new


class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        # 直接暴力
        while len(nums)!=1:
            new_nums=[0]*(len(nums)//2)
            for i,v  in enumerate(new_nums):
                if i%2==0:
                    new_nums[i]=min(nums[2*i],nums[2*i+1])
                else:
                    new_nums[i]=max(nums[2*i],nums[2*i+1])
            nums=new_nums
        return nums[0]
        # 优化点在于可以直接原地变换
# @lc code=end

