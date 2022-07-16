import heapq
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        dvi = []
        for each in hand:
            heapq.heappush(dvi, each)
        count = len(hand) // groupSize
        ans = [[-1, 0] for i in range(count)]
        while dvi:
            item = heapq.heappop(dvi)
            flag = False
            for each in ans:
                if each[1] == groupSize:
                    continue
                elif each[1] == 0:
                    each[0], each[1] = item, 1
                    flag=True
                    break
                elif each[0] == item - 1:
                    each[0], each[1] = item, each[1] + 1
                    flag=True
                    break
            if not flag:
                return False
        return True

Solution().isNStraightHand(
[1,2,3,6,2,3,4,7,8],
3)