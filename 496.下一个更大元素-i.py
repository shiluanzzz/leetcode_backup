#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
import collections


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans={}
        stack=[]
        # 维护一个递减的单调栈
        for i in nums2:
            while stack and i>stack[-1]:
                ans[stack.pop()]=i
            stack.append(i)
        res=[]
        for i in nums1:
            if not ans.get(i):
                res.append(-1)
            else:
                res.append(ans[i])
        return res
# @lc code=end

