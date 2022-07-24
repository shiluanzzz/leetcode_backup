#
# @lc app=leetcode.cn id=1632 lang=python3
#
# [1632] 矩阵转换后的秩
#

# @lc code=start
import heapq
import collections
class Solution:
    # 第一个版本里最大的问题在于 如果两个值是一样的，那这两个值取处理然后对比大小分到的rank可能不一样。
    def matrixRankTransform_1(self, matrix: list[list[int]]) -> list[list[int]]:
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
    
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        R,C = len(matrix),len(matrix[0])
        ans=[[0]*C for _ in range(R)]
        # 全部的值进行排序
        dv=collections.defaultdict(list)
        for i in range(R):
            for j in range(C):
                dv[matrix[i][j]].append((i,j))
        R_count,C_Count=[0]*R,[0]*C
        for key in sorted(dv.keys()):
            # 踩坑：只有在同一行或者同以列才有相同的rank
            # @TODO 还是没做出来
            rank=1
            for i,j in dv[key]:
                rank=max(R_count[i]+1,rank)
                rank=max(C_Count[j]+1,rank)
            for i,j in dv[key]:
                ans[i][j]=rank
                R_count[i]=max(R_count[i],rank)
                C_Count[j]=max(C_Count[j],rank)
        return ans

# @lc code=end

# print(Solution().matrixRankTransform([[4,4,4],[4,4,4]]))
# print(Solution().matrixRankTransform([[1]]))
# print(Solution().matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))
print(Solution().matrixRankTransform([[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]]))