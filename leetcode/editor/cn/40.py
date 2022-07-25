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
# 先计数，在替代后插入，求解时在解码
def solve(candidates:list,target):
    # 分治法
    candidates.sort()
    res =[]

    def d(sum,ans,index):
        if sum==target:
            if ans not in res:
                res.append(ans)
            return

        for d_index,each in enumerate(candidates[index:]):
            if sum+each==target:
                ans.append(each)
                if ans not in res:
                    res.append(ans.copy())
                return
            elif sum+each>target:
                return
            else:
                t=ans.copy()
                t.append(each)
                if len(candidates)-(index+d_index+1)<(target-sum-each):
                    return
                else:
                    d(sum+each,t,index+d_index+1)

    for index,i in enumerate(candidates):
        d(i,[i],index+1)
    print(res)
    return res
# @lc code=end

print(Solution().combinationSum2([1]*27,26))