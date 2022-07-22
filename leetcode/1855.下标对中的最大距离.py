#
# @lc app=leetcode.cn id=1855 lang=python3
#
# [1855] 下标对中的最大距离
#

# @lc code=start
from tokenize import maybe


class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        ans=0
        for i in range(len(nums1)):
            for j in range(len(nums2)-1,-1,-1):
                maybe_ans=j-i
                if maybe_ans<=ans or nums2[j]<nums1[i]:
                    break
                if j>=i and nums2[j]>=nums1[i]:
                    ans=j-i
        return ans
# @lc code=end

