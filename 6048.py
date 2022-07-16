import collections
#  [3,4,2,3,4,7]
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:

        hash=collections.defaultdict(int)
        ans=float("inf")
        for i,v in enumerate(cards):
            if v in hash:
                ans=min(ans,i-hash[v]+1)
            hash[v]=i
        return ans if ans!=float('inf') else -1
