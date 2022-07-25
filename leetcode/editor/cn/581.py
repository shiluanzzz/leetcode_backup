#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        stack=[] #index
        ans=[]
        # for i,v in enumerate(nums):
        for i in range(len(nums)):
            temp=[]
            while len(stack) and nums[i]<nums[stack[-1]]:
                # 出现逆序 需要重新排序
                temp.append(stack.pop())
            stack.append(i)
            if temp:
                ans.append(temp[-1])
            stack.extend(temp)
        if len(ans)>1:
            # 每次记录的是出现逆序的前一个占位，+1 长度+1
            return ans[-1]-ans[0]+2
        elif len(ans)==1:
            return 2
        else:
            return 0
# @lc code=end

print(Solution().findUnsortedSubarray([2,6,4,8,10,9,15]))
print(Solution().findUnsortedSubarray([2,3,4,8,10,9,15]))
print(Solution().findUnsortedSubarray([2,3,4,8,7,10,9,15]))