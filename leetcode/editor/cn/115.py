#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        dp=[[0]*(m+1) for _ in range(n+1)]
        # dp[i][j] 表示 s[:i]中 子序列为t[:j]的个数
        for i in range(0,n+1):
            for j in range(0,m+1):
                # 空字符串肯定是一个子序列
                if j==0: dp[i][j]=1
                elif i==0: dp[i][j]=0
                else:
                    if s[i-1]==t[j-1]:
                        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j]
        return dp[n][m]
# @lc code=end

print(Solution().numDistinct(
    "babgbag",
    "bag"
))