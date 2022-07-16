# 54. 螺旋矩阵


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
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


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().spiralOrder([
        [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
    ]))
