# 创建时间:2022-08-31 18:30:40


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    #
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] 表示 s[i:j+1] 是否为回文串
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = 1
        ans_s = s[0]
        for L in range(2, len(s) + 1):
            for i in range(n):
                # j-1 就是右边界的位置
                j = i + L - 1
                if j >= len(s): break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 如果前后两端相等，也需要分情况讨论
                    if L <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and L > ans:
                    ans = L
                    ans_s = s[i:j + 1]
        return ans_s

    # 之前的答案
    def longestPalindrome_h1(self, s: str) -> str:
        # review:面向解析做题
        # dp[i][j] 标记字符串s[i:j+1]是不是回文字符串
        # dp[i][j]的转移方程就取决与s[i]是否等于s[j] 以及 dp[i+1][j-1] 也就是里面那个字符串是不是回文字符串
        # 方向对了 但是还是没完全想明白
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        max_lens = 1
        begin = 0
        # 枚举子串的长度，更长的子串的转移是基于短串的转移，所以是先枚举子串的长度
        for L in range(2, len(s) + 1):
            for i in range(len(s)):
                # 右边界
                j = i + L - 1
                if j >= len(s): break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 记录当前最长的回文子串
                if dp[i][j] and L > max_lens:
                    max_lens, begin = L, i
        return s[begin:begin + max_lens]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
