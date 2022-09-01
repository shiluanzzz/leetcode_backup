# 创建时间:2022-09-01 15:19:20


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        nums = [0] * 31
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]
        print(nums)
        return nums[n]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    30
    """
    from leetcode import tools

    tools.test_func_batch(Solution().fib, params)
