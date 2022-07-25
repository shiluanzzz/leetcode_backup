#
# @lc app=leetcode.cn id=2262 lang=python3
#
# [2262] 字符串的总引力
#

# @lc code=start
class Solution:
    def appealSum(self, s: str) -> int:
        # reivew 面向解析做的 TODO 没理解
        # dp[i] 表示以第i个字符为结尾的字符串总引力
        dp=[0]*len(s)
        d={}
        for i,v in enumerate(s):
            dp[i] -= d.get(v,-1)
            dp[i] += dp[i-1] + i
            d[v]=i
        return sum(dp)
# @lc code=end

