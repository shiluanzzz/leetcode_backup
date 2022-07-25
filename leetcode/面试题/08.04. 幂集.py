import collections
from pip import main


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # 所有非重复的子集
        # 踩坑：没认真读题，这样只能求出连续的子集 对于[1,2,3],求不出[1,3]
        # @review: dfs的写法还不熟练
        ans=[]
        def dfs(i:int,now_set:list):
            # 以i为开始的起点
            if i==len(nums):
                ans.append(now_set[:])
            else:
                dfs(i+1,now_set)
                dfs(i+1,now_set+[nums[i]])
        dfs(0,[])
        return [list(i) for i in ans]+[[]]
    
    def solve2(self,nums:list[int]):
        # 踩坑 时间复杂度太高了
        # @TODO用装饰器实现往list中插入一个不重复的值
        ans=[]
        for num in nums:
            new_ans=[]
            for i in ans:
                    new_ans.append((list(i)+[num]))
            ans.append([num])
            ans.extend(new_ans)
        return [list(i) for i in ans]
    # @TODO 二进制枚举如何做？
print(Solution().subsets([i for i in range(10)]))