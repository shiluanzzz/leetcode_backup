# 创建时间:2022-09-01 15:15:46


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Review
        # 分两种情况 到第i天持有股票和到第i天不持有股票的最大收益
        dp1 = [0] * len(prices)  # 不持有
        dp2 = [0] * len(prices)  # 持有
        dp2[0] = -prices[0]
        for i in range(1, len(prices)):
            dp2[i] = max(dp2[i - 1], dp1[i - 1] - prices[i])  # 持有股票
            dp1[i] = max(dp1[i - 1], dp2[i - 1] + prices[i])  # 从不持有股票的状态转移过来
        return dp1[len(prices) - 1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    [7,1,5,3,6,4]
    [1,2,3,4,5]
    [7,6,4,3,1]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().maxProfit, params)
