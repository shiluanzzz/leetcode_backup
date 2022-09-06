# 创建时间:2022-09-06 15:50:19

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 26进制
        # c = [chr(ord('A') + i) for i in range(26)]
        ans = ""
        while columnNumber > 0:
            mod = columnNumber % 26
            if mod == 0:
                columnNumber -= 26
                mod = 26
            columnNumber //= 26
            ans += chr(ord('A') + mod - 1)
            # ans = c[mod] + ans
        # ans += c[columnNumber] + ans
        return ans[::-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    1
    28
    52
    701
    2147483647
    """
    from leetcode import tools

    tools.test_func_batch(Solution().convertToTitle, params)
