#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        self.ans=set()
        n=len(nums)
        def back(i,t):
            # if i==n:
            #     print(t)
            if len(t)>=2 and tuple(t) not in self.ans:
                # print(t)
                self.ans.add(tuple(t.copy()))
            for j in range(i,n):
                if len(t) and nums[j]<t[-1]:continue
                t.append(nums[j])
                back(j+1,t)
                t.pop()
        back(0,[])
        return list(map(list,self.ans))
# @lc code=end

print(Solution().findSubsequences([4,6,7,7]))