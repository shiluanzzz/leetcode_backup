# 创建时间:2022-09-01 11:14:39


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 买卖一次股票!!! 不是可以买多次 看清题意！！！
        ans, min_v = 0, float('inf')
        for v in prices:
            min_v = min(min_v, v)
            ans = max(ans, v - min_v)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    [7,1,5,3,6,4]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().maxProfit, params)
