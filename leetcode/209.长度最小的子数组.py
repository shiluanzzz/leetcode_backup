#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
import itertools


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = float('inf')
        pre_sum = list(itertools.accumulate(nums))
        for i,v in enumerate(pre_sum):
            if nums[i]>=target:return 1
            if v>=target:
                ans=min(ans,i+1)
                # 每次都从第一个位置往前找肯定会超时，找出一个可能最短位置开始判断。
                begin = i+1-ans
                for j in range(begin,i-1):
                    if pre_sum[i]-pre_sum[j]>=target:
                        ans=min(ans,i-j)
                    else:
                        break
                # 从后往前，在做一个剪枝
                        
        return ans if ans != float('inf') else 0
# @lc code=end

print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))