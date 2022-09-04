# 创建时间:2022-09-01 10:21:50


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK1(self, nums: list[int], k: int) -> int:
        self.ans = 0

        # 这种暴力应对 3000长度的数据肯定会超时
        def dfs(cum: int, begin: int):
            if begin >= len(nums): return
            if cum * nums[begin] < k:
                self.ans += 1
                dfs(cum * nums[begin], begin + 1)
                return

        for i in range(len(nums)):
            dfs(1, i)
        return self.ans

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # Review 必须使用滑动窗口的思想
        ans, left, cur = 0, 0, 1  # left 左窗口，cur 当前窗口下的乘积和
        for right, val in enumerate(nums):
            cur *= val
            # 这个while 就是当前右窗口下的最大窗口
            while left <= right and cur >= k:
                cur //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    [8, 2, 9, 4, 3, 10, 5, 7, 8, 8]
    100
    [10,5,2,6]
    100
    """
    from leetcode import tools
    import random

    params += str([random.randint(1, 10) for _ in range(3000)]) + "\n"
    params += "100"
    tools.test_func_batch(Solution().numSubarrayProductLessThanK, params)
