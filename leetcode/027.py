# -*- coding:utf-8 -*-
# __author__ = "shitou6"

class Solution:
    def removeElement(self, nums, val):
        q=0
        p=0
        while(p<len(nums)):
            if nums[p]==val:
                p+=1
            else:
                nums[q]=nums[p]
                q,p=q+1,p+1
        print(nums[:q])
        return q
    # 倒序遍历
    def removeElement2(self, nums:list, val):
        for i in range(len(nums)-1,-1,-1):
            # 9 8 7
            if nums[i]==val:
                nums.pop(i)
        return len(nums)

s=Solution()

print(s.removeElement([0,1,2,2,3,0,4,2],2))
