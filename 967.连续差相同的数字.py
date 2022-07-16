#
# @lc app=leetcode.cn id=967 lang=python3
#
# [967] 连续差相同的数字
#

# @lc code=start
from traceback import print_tb


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        # 181 292 7
        ans=[]
        def dfs(num,pre,depth):
            ans=[]
            if depth>=n:
                return [num]
            num*=10
            if pre+k<10:
                ans.extend(dfs(num+pre+k,pre+k,depth+1))
            if pre>=k and pre+k!=pre-k:
                ans.extend(dfs(num+pre-k,pre-k,depth+1))
            return ans
        
        for i in range(1,10):
            print(i,dfs(i,i,1))
            ans.extend(dfs(i,i,1))
        return ans
# @lc code=end

print(Solution().numsSameConsecDiff(4,0))