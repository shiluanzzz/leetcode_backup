#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: list[int], b: int) -> int:
        i,a=float('inf'),0
        for k in nums:
           i=min(i,k)
           a=max(a,k)
        diff=a-i
        return max(0,diff-2*b)

# @lc code=end

print(Solution().smallestRangeI([0,10],2))