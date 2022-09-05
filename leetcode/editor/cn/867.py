# 创建时间:2022-09-05 16:18:48

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n, m = len(matrix), len(matrix[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i]=matrix[i][j]
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
    # tools.test_func_batch(Solution()., params)
