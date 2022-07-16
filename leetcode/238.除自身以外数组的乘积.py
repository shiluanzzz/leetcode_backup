#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 前缀乘 * 后缀乘
        ans=[1]*len(nums)
        pre_x_sum = [1]*len(nums)
        for i in range(1,len(nums)):
            pre_x_sum[i]=nums[i-1]*pre_x_sum[i-1]
        back_x_sum = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            back_x_sum[i]=nums[i+1]*back_x_sum[i+1]
        for i in range(len(nums)):
            ans[i]=pre_x_sum[i]*back_x_sum[i]
        return ans

# @lc code=end

