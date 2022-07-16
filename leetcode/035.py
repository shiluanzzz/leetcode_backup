# -*- coding:utf-8 -*-
# __author__ = "shitou6"

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        # 折半查找
        left,right=0,len(nums)
        while left<right:
            # mid=(right+left)//2 这样写可能导致大数溢出
            mid= left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left if left<right else right

    def searchInsert2(self, nums: list, target: int) -> int:
        for i in nums:
            if i>=target:return nums.index(i)
        return len(nums)




s=Solution()
print(s.searchInsert2([1,3,5,6],2))
