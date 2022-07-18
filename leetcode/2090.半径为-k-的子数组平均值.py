#
# @lc app=leetcode.cn id=2090 lang=python3
#
# [2090] 半径为 k 的子数组平均值
#

# @lc code=start
import enum


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k==0:return nums
        if 2*k+1>len(nums):
            return [-1]*len(nums)
        ans=[]
        base=sum(nums[:2*k+1])
        for i,v in enumerate(nums[k:-k],k):
            ans.append(base//(2*k+1))
            base-= nums[i-k]
            if (i+k+1)<len(nums):
                # review 这个i+k+1 想了半天
                base+=nums[i+k+1]
            else:
                break
        ans=[-1]*k+ans+[-1]*k
        return ans
        
# @lc code=end

# print(Solution().getAverages([7,4,3,9,1,8,5,2,6],1))
print(Solution().getAverages([40527,53696,10730,66491,62141,83909,78635,18560],2))