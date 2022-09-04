import collections


class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        idx = collections.defaultdict(int)
        for i, v in enumerate(s):
            idx[v] = i - idx[v]
        for k, v in idx.items():
            if distance[ord(k) - ord('a')] != v - 1:
                return False
        return True