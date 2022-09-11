# 创建时间:2022-09-08 23:05:08

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp: s的前i个字符串可以有几种解码方法,
        # 最后的结果想到与s加上一个空字符串
        dp = [1] + [0] * len(s)
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i - 2 >= 0 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[- 1]
    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    "12"
    "226"
    "0"
    "10"
    "12"
    """
    from leetcode import tools

    tools.test_func_batch(Solution().numDecodings, params)
