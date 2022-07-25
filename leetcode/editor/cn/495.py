#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
import enum
from time import time


class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        ans=0
        for i,v in enumerate(timeSeries):
            if i!=len(timeSeries)-1:
                ans += min(duration,timeSeries[i+1]-v)
            else:
                ans += duration
        return ans
# @lc code=end

