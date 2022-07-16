#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#

# @lc code=start
class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        
        dp=[[0]*(target+1) for _ in range(10)]
        where=[[0]*(target+1) for _ in range(10)]
        for i in range(target):
            dp[0][i]=-float("inf")
        # where不用记录i，因为当转移自j时那肯定从i-1来的，否则就是从i来的
        dp[0][0]=0
        for i,c in enumerate(cost,1):
            for j in range(target+1):
                if c>j:
                    dp[i][j]=dp[i-1][j]
                    where[i][j]=j
                else:
                    if dp[i-1][j]>dp[i][j-c]+1:
                        dp[i][j]=dp[i-1][j]
                        where[i][j]=j
                    else:
                        dp[i][j]=dp[i][j-c]+1
                        where[i][j]=j-c
        if dp[9][target]<=0:return "0"
        print(dp)
        ans=[]
        i,j=9,target
        while i>0:
            if j==where[i][j]:
                # 从i-1转移来的
                i-=1
            else:
                ans.append(str(i))
                j=where[i][j]
        return "".join(ans)

# @lc code=end
print(Solution().largestNumber(
    [2,4,6,2,4,6,4,4,4],
5
))
