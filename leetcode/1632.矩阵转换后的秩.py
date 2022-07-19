#
# @lc app=leetcode.cn id=1632 lang=python3
#
# [1632] 矩阵转换后的秩
#

# @lc code=start
import heapq
from re import A
class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        ans=[[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
        h=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(h,[matrix[i][j],i,j])
        while h:
            t=heapq.heappop(h)
            num,i,j=t[0],t[1],t[2]
            flag=1 # 标记数是否相等
            temp=0
            for k in range(len(matrix)):
                if ans[k][j]>temp:
                    temp=ans[k][j]
                    if matrix[k][j]!=num:
                        flag=1
                    else:
                        flag=0
            for k in range(len(matrix[0])):
                if ans[i][k]>temp:
                    temp=ans[i][k]
                    if matrix[i][k]!=num:
                        flag=1
                    else:
                        flag=0
            ans[i][j]=temp+flag
        return ans

# @lc code=end

print(Solution().matrixRankTransform([[4,4,4],[4,4,4]]))
print(Solution().matrixRankTransform([[1]]))
print(Solution().matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))
