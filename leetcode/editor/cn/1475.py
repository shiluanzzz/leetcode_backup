# 创建时间:2022-09-01 09:31:41


# leetcode submit region begin(Prohibit modification and deletion)
import bisect


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ans = []
        for i, v in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= v:
                    ans.append(v - prices[j])
                    break
            if len(ans) == i: ans.append(v)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    [8,4,6,2,3]
    [1,2,3,4,5]
    [10,1,1,6]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().finalPrices, params)
