# 846. 一手顺子


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        c=collections.Counter(hand)
        for start in sorted(c.keys()):
            if not c[start]:continue
            count=c[start]
            for end in range(start,start+groupSize):
                if c[end]<count:
                    return False
                c[end]-=count
        return True

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().isNStraightHand([1,2,3,3,4,4,5,6]
,4))