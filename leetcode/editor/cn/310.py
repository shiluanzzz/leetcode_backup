from webbrowser import get


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # n的数量级有点大，用矩阵存肯定不行
        martix=[[0 for _ in range(n)] for _ in range(n)]
        for items in edges:
            martix[items[0]][items[1]]=1
            martix[items[1]][items[0]]=1
        path_sum=[sum(i) for i in martix]
        ans,val=[],float('inf')
        print(path_sum)
        print(martix)
        def get_max_height(fo,i,MAX):
            lens=0
            for index,v in enumerate(martix[i]):
                if index==fo:continue
                if v:
                    lens=max(lens,get_max_height(i,index,MAX)+1)
                    if lens>MAX:return lens
            return lens
        for i in range(n):
            s=get_max_height(-1,i,val)
            if s<val:
                ans,val=[i],s
            elif s==val:
                ans.append(i)
            print("{}:{}".format(i,s))
        return ans
                
print(Solution().findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))