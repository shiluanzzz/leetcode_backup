#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            print(l,mid,r)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
                mid=(l+r)//2
            else:
                l=mid+1
                mid=(l+r)//2
        return -1
# @lc code=end

print(Solution().search([-1,0,3,5,9,12],9))