# 747. 至少是其他数字两倍的最大数


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        m=max(nums)
        for i in nums:
            if i*2>m:return -1
        return nums.index(m)

# leetcode submit region end(Prohibit modification and deletion)
