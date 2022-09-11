# -*- coding:utf-8 -*-
# __author__ = "shitou6"
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3

# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    # time: 2022-09-09 11:12:02
    def findLength(self, A: list, B: list) -> int:
        # dp[i][j] 表示 A[i:]与B[j:]的最长公共前缀
        # dp[i][j] = dp[i+1][j+1] if A[i]==B[j]
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        ans = 0
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    ans = max(ans, dp[i][j])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

from leetcode import tools

params = """
        [1, 2, 3, 2, 1, 313, 3, 3, 3, 3, 1, 1, 3, 4, 4, 5, 6, 1, 5, 1, 4, 2, 4, 5, 2, 4, 5, 4, 2, 4],
        [3, 2, 1, 4, 7]
        [3, 2, 1, 4, 7]
        [3, 2, 1, 4, 7]
        [1,2,3,2,1]
        [3,2,1,4,7]
        [1,2,3,2,1]
        [3,2,1,4]
"""
tools.test_func_batch(Solution().findLength,params)


def findLength(A: list, B: list) -> int:
    max = 0
    l = len(A) if len(A) > len(B) else len(B)
    for i in range(1, l + 1):
        indexb = len(B) - i if len(B) - i > 0 else 0
        each = findMaxLength(A[0:i if i <= len(A) else len(A)],
                             B[indexb:])
        max = each if each > max else max
    a = A
    b = B
    for i in range(1, l + 1):
        indexb = len(a) - i if len(a) - i > 0 else 0
        each = findMaxLength(b[0:i if i <= len(b) else len(b)],
                             a[indexb:])
        max = each if each > max else max
    print(max)
    return max


def findMaxLength(a, b):
    print("a:" + str(a))
    print("b:" + str(b))

    if a == b:
        return len(a)
    elif a in b:
        return len(a)
    elif b in a:
        return len(b)
    return 0

# if __name__ == '__main__':
#     findLength(
#         [1, 2, 3, 2, 1, 313, 3, 3, 3, 3, 1, 1, 3, 4, 4, 5, 6, 1, 5, 1, 4, 2, 4, 5, 2, 4, 5, 4, 2, 4],
#         [3, 2, 1, 4, 7]
#     )
