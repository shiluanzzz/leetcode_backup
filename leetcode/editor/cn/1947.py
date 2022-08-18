# 1947.最大兼容性评分和
# 创建时间: 2022-08-05 15:17:32

# leetcode submit region begin(Prohibit modification and deletion)
import collections
import functools
from itertools import permutations


class Solution:
    def maxCompatibilitySum(self, students: list[list[int]], mentors: list[list[int]]) -> int:
        @functools.lru_cache()
        def score(a, b):
            a, b = eval(a), eval(b)
            t = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    t += 1
            return t

        # def to_num(a):
        #     res = 0
        #     for i in a:
        #         res += i
        #         res *= 10
        #     return res // 10

        ans = 0
        for i in permutations(range(0, len(students))):
            t = 0
            for j, v in enumerate(i):
                t += score(str(students[j]), str(mentors[v]))
            print(i, t)
            ans = max(ans, t)
        return ans
    # leetcode submit region end(Prohibit modification and deletion)


# main
if __name__ == "__main__":
    import sys

    # sys.path.append("D:\\project\\PyProject\\leetcode_record\\")
    # import tools
    #
    # tools.test_func(Solution().xxx)
    Solution().maxCompatibilitySum([[1, 1, 0], [1, 0, 1], [0, 0, 1]],
                                   [[1, 0, 0], [0, 0, 1], [1, 1, 0]])
