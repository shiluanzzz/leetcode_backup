#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
# from curses.ascii import SO
from functools import lru_cache


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # 二维前缀和
        if len(matrix)==0:return 0
        row,col=len(matrix),len(matrix[0])
        pre_sum=[[0]*col for _  in range(row)]
        for i in range(0,row):
            for j in range(0,col):
                if i==0 and j==0:pre_sum[i][j]=int(matrix[i][j])
                elif i==0:
                    pre_sum[i][j]+=(pre_sum[i][j-1]+int(matrix[i][j]))
                elif j==0:
                    pre_sum[i][j]+=(pre_sum[i-1][j]+int(matrix[i][j]))
                else:
                    pre_sum[i][j]=pre_sum[i-1][j]+pre_sum[i][j-1]-pre_sum[i-1][j-1]+int(matrix[i][j])
        self.ans=0

        @lru_cache(None)
        def cal(i,j,q,w):
            # print(i,j,q,w)
            if q>=row or w>=col:return False
            # if q<=i or w<=j:return False
            # 1,2 3,4
            need=(q-i+1)*(w-j+1)
            true=pre_sum[q][w]
            if i-1>=0:
                true-=pre_sum[i-1][w]
            if j-1>=0:
                true-=pre_sum[q][j-1]
            if i>=1 and j>=1:
                true+=pre_sum[i-1][j-1]
            if need==true:
                self.ans=max(self.ans,need)
                return True
            else:
                return False
        
        for i in range(row):
            for j in range(col):
                if i==0 and j==0:
                    self.ans=pre_sum[0][0]
                    continue
                if matrix[i][j]==0:
                    continue
                for x_diff in range(i,row):
                    # if matrix[x_diff][j]!='1':
                        # break
                    for y_diff in range(j,col):
                        if not cal(i,j,x_diff,y_diff):
                            break
        cal.cache_clear()
        return self.ans
# @lc code=end

print(Solution().maximalRectangle(
    [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
))
print(Solution().maximalRectangle(
[
    [0,0,1,0],
    [0,1,1,1],
    [0,1,1,1]
]
))
t=[]
for i in range(201):
    t.append([1]*200)
print(Solution().maximalRectangle(t))