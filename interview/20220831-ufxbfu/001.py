
class Solution:
    def ncov_defect(self , grid ):
        # write code here
        if len(grid)==0:return 0
        ans=0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=1: continue
                if i-1>=0 and grid[i-1][j]==0:
                    grid[i-1][j]=2
                    ans+=1
                if i+1<m and grid[i+1][j]==0:
                    grid[i+1][j]=2
                    ans+=1
                if j-1>=0 and grid[i][j-1]==0:
                    grid[i][j-1]=2
                    ans+=1
                if j+1<n and grid[i][j+1]==0:
                    grid[i][j+1]=2
                    ans+=1
        for i in grid:
            print(i)
        return  ans

print(Solution().ncov_defect(
[[0,1,0,0,0,0,0,1], [0,1,0,0,0,0,0,1], [0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0]]
))