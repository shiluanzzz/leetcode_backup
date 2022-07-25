#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start

from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)
        dp=[[0]*(n+1) for _ in range(m+1)]
        before=""
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i]==p[j] or p[j]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j]=='*':
                    # 分三种情况:
                    if p[j-1]!=s[i]: #不匹配上一个字符
                        # ab  abc* 对c匹配0次
                        dp[i][j]=dp[i][j-2]
                    elif p[j-1]==s[i] or p[j-1]=='.':
                        # 匹配上了
                        dp[i][j]=dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j]=0
        return dp[n][m]
# @lc code=end

