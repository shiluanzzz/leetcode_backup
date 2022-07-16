# 560. {question.title}


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        pre_sum=[0]*len(nums)
        for i,v in enumerate(nums):
            if i==0:
                pre_sum[i]=v
            else:
                pre_sum[i]=pre_sum[i-1]+v
        for i in range(len(nums)):

# leetcode submit region end(Prohibit modification and deletion)
