#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#

# @lc code=start
import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # 先排序
        trips.sort(key=lambda x:x[1])
        passenger = []
        nums=0
        for i in trips:
            while passenger:
                temp=heapq.heappop(passenger)
                if temp[0]<=i[1]: # 可以下车
                    nums-=temp[-1]
                else:
                    heapq.heappush(passenger,temp)
                    break
            if nums+i[0]>capacity:
                return False
            heapq.heappush(passenger,[i[2],i[1],i[0]])
            nums+=i[0]
        return True

# @lc code=end

print(Solution().carPooling([[2,1,5],[3,3,7]],4))
print(Solution().carPooling([[2,1,5],[3,3,7]],5))
print(Solution().carPooling([[2,1,3],[3,3,7]],3))
print(Solution().carPooling([[2,1,3],[1,2,5],[3,3,7]],4))
print(Solution().carPooling([[7,5,6],[6,7,8],[10,1,6]],16))