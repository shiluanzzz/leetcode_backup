# -*- coding:utf-8 -*-
# __author__ = "shitou6"
class Solution:
    def maxSubArray(self, nums: list) -> int:
        # 暴力求解
        sum=nums[0]
        max_= sum
        for i in range(1,len(nums)):
            if sum+nums[i]>nums[i]:#本质就是判断下一个元素是不是大于0 是的话就可能出现更长的数组和
                max_=max(max_,sum+nums[i])

s=Solution()
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

def solve(nums):
    sum=nums[0]
    ans=[nums[0]]
    temp_sum=nums[0]
    temp_ans=[nums[0]]
    i,n=1,len(nums)
    max_z_index=0   # 最大的正数的index
    while i<n:
        if nums[i]>0 and i>max_z_index:
            max_z_index=i
        if nums[i]>0 and temp_sum<0:
            temp_ans=[nums[i]]
            temp_sum=nums[i]
        else:
            # 如果遇到负数，可以将其与前面的正数融合视作为一个正数。
            if nums[i]+temp_sum>=0:
                temp_ans.append(nums[i])
                temp_sum+=nums[i]
            else:
                temp_sum=nums[i]
                temp_ans=[nums[i]]
        if temp_sum>sum:
            sum=temp_sum
            ans=temp_ans.copy()
        i+=1
    return ans

print(solve([-2,1,-3,4,-1,2,1,-5,4]))
print(solve([-2,1,1,-1,4,5]))
print(solve([-1999]))
print(solve([-1]))
print(solve([1]))