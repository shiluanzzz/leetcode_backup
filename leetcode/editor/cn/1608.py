# 创建时间:2022-09-12 11:53:42

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        # 特征值只可能在[1,n]中
        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i == n or nums[i] < i):
                return i
        return -1

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
    # tools.test_func_batch(Solution()., params)
