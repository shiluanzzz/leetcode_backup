# 创建时间:2022-09-01 15:39:18


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # review 面向解析做题
        # 题目给出了条件，就是在买一只股票进来的时候必须不持有股票，且最大的买卖次数为两次，所以转移状态是固定的
        # 五种状态 没买，买1只，买了一只卖了一只 ，买卖一次，买一次，买卖两次
        dp1, dp2, dp3, dp4 = -prices[0], 0, -prices[0], 0
        for v in prices[1:]:
            # 对于只买一只，最好的情况就是反悔，买一只价格更低的股票
            dp1 = max(dp1, -v)
            # dp2 以更高的价格卖出去
            dp2 = max(dp2, dp1 + v)
            dp3 = max(dp3, dp2 - v)
            dp4 = max(dp4, dp3 + v)
        return dp4


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

