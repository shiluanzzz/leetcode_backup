# 创建时间:2022-09-07 19:41:35

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def generate(s, left, right):
            if len(s) == n * 2:
                ans.append(s)
                return
            if left < n:
                generate(s + "(", left + 1, right)
            if right < left:
                generate(s + ")", left, right + 1)
            return

        generate("", 0, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    3
    1
    2
    8
    """
    from leetcode import tools

    tools.test_func_batch(Solution().generateParenthesis, params)
