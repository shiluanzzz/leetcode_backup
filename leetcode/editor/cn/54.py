# 54. 螺旋矩阵


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder2(self, matrix: list[list[int]]) -> list[int]:
        l, r, t, b = -1, len(matrix[0]), -1, len(matrix)
        i, j = 0, 0
        ans = []
        target_lens = len(matrix) * len(matrix[0])
        while t < b and l < r:
            while j < r:
                ans.append(matrix[i][j])
                j += 1
            i, j, t = i + 1, j - 1, t + 1
            if len(ans) == target_lens: break
            while i < b:
                ans.append(matrix[i][j])
                i += 1
            i, j, r = i - 1, j - 1, r - 1
            if len(ans) == target_lens: break
            while j > l:
                ans.append(matrix[i][j])
                j -= 1
            i, j, b = i - 1, j + 1, b - 1
            if len(ans) == target_lens: break
            while i > t:
                ans.append(matrix[i][j])
                i -= 1
            i, j, l = i + 1, j + 1, l + 1
            if len(ans) == target_lens: break
        return ans

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, right, down, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        ans = []
        while top <= down and right >= left:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            for i in range(down, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        lens = len(matrix) * len(matrix[0])
        return ans[:lens]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    params = """
    [[6,7,9]]
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    [[1,2,3],[4,5,6],[7,8,9]]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().spiralOrder, params)
