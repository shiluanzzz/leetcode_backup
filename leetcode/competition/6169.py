import random
from functools import lru_cache


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        ans = 0
        for i, v in enumerate(nums):
            j = i - 1
            while j > 0 and (v & nums[j]) == 0:
                v |= nums[j]
                j -= 1
            ans = max(ans, i - j)
        return ans

class Solution2:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        @lru_cache
        def AND(a, b):
            return a & b

        ans = 1
        for i in range(len(nums)):
            max_lens = len(nums) - i
            if max_lens <= ans:
                return ans
            arr = set()
            arr.add(nums[i])
            for j in range(i + 1, len(nums)):
                if nums[j] in arr:
                    break
                ok = True
                for cur in arr:
                    if AND(nums[j], cur):
                        ok = False
                        break
                if ok:
                    arr.add(nums[j])
                else:
                    break
            ans = max(ans, len(arr))
        return ans
        # # self.ans = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if AND(nums[i], nums[j]):
        #
        # # 枚举
        # for L in range(len(nums), 1, -1):
        #     for i in range(0, len(nums) - L + 1):
        #         if judge(nums[i:L + i]):
        #             return L
        # return 1
        #
        # # 优化的点在于 子数组要连续
        # # num[i] num[j] ->


from leetcode.tools import test_func_batch

params = """
[1,3,8,48,10]
[3,1,5,11,13]
"""
params += str([random.randint(1, 10) for _ in range(10000)])
test_func_batch(Solution().longestNiceSubarray, params)
