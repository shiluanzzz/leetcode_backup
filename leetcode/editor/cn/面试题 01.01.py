# 创建时间:2022-09-05 15:53:09

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for char in astr:
            if (mark & (1 << (ord(char) - ord('a')))) != 0:
                return False
            mark |= 1 << (ord(char) - ord('a'))
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
    # tools.test_func_batch(Solution()., params)
