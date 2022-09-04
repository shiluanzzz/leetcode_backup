import functools


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        max_num = 10 ** 9 + 7

        @functools.cache
        def go(x, step):  # 在x位置,还剩下step步,走到endpos有几种方案
            if abs(x - endPos) > step: return 0
            if step <= 0: return 1
            return (go(x - 1, step - 1) + go(x + 1, step - 1)) % max_num

        return go(startPos, k)


print(Solution().numberOfWays(1, 2, 3))
