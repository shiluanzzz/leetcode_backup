#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        print(candidates)
        n=len(candidates)
        used=[0]*n
        candidates.sort()
        def back(k,path,sum):
            if sum==target:
                self.ans.add(tuple(path.copy()))
            if sum>target:
                return False
            for i,v in enumerate(used):
                if i<k or v:continue
                if i>k and candidates[i-1]==candidates[i]:break
                path.append(candidates[i])
                sum+=candidates[i]
                used[i]=1
                back(i,path,sum)
                used[i]=0
                path.pop()
                sum-=candidates[i]
        self.ans=set()
        back(0,[],0)
        return list(map(list,self.ans))
# @lc code=end

print(Solution().combinationSum2([1]*27,26))