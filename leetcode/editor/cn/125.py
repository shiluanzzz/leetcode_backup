# 创建时间:2022-09-06 15:45:07


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for i in s:
            if i >= 'a' and i <= 'z':
                ss += i
            if i >= 'A' and i <= 'Z':
                ss += chr(ord('a') + ord(i) - ord('A'))
            if i >= '0' and i <= '9':
                ss += i
        return ss == ss[::-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    "A man, a plan"
    "ABabbaBA"
    "AB001100ba"
    """
    from leetcode import tools
    tools.test_func_batch(Solution().isPalindrome, params)
