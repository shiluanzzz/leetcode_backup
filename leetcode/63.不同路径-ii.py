#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n,m=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0]*m for _ in range(n)]
        dp[0][0]=1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i==0 and j==0:continue
                    if i-1>=0:
                        dp[i][j]+=dp[i-1][j]
                    if j-1>=0:
                        dp[i][j]+=dp[i][j-1]
        return dp[n-1][m-1] 
                
# @lc code=end

print(Solution().uniquePathsWithObstacles([
    [0,0,0]
]))