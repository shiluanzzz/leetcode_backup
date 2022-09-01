import collections
from operator import ne


class Solution:
    def minimumRounds1(self, tasks: list[int]) -> int:
        count = list(collections.Counter(tasks).values())
        print(count)
        ans = 0
        for i in range(len(count)):
            if count[i] < 2:
                return -1
            if count[i] % 3 == 0:
                pass
            elif count[i] % 3 == 1:
                ans += 1
                count[i] -= 4
            else:
                ans += 1
                count[i] -= 2
            ans += count[i] // 3
        return ans

    def minimumRounds(self, tasks: list[int]) -> int:
        # 想要最少 那肯定是优先一下子做三个
        counter = collections.Counter(tasks)
        ans = 0
        for v in counter.values():
            if v == 1: return -1
            if v % 3 == 0:
                ans += v // 3
            else:
                # 4 = 3+1 = 2+2
                # 2 = 0+2 = 2
                ans += (v // 3 + 1)
        return ans

