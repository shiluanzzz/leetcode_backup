import collections
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        cnt = [0] * n #这种跟堆无关的变量，不需要放到堆里面
        room, using = list(range(n)), []
        for begin, end in meetings:
            # 堆的[0]一定是最小的，可以直接访问
            while using and using[0][0] <= begin:
                heapq.heappush(room, heapq.heappop(using)[1])
            if len(room):
                idx = heapq.heappop(room)
            else:
                item = heapq.heappop(using)
                end = item[0] + end - begin
                idx = item[1]
            cnt[idx] += 1
            heapq.heappush(using, (end, idx))
        print(cnt)
        return cnt.index(max(cnt))

class Solution1:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        meets = []  # 序号，结束时间，使用次数
        holds = []  # 结束时间,使用次数,序号
        for i in range(n):
            heapq.heappush(meets, [i, 0, 0])
        ans, count = float('inf'), 0
        for v in meetings:
            while holds:
                # 已经开完会的放回到空闲会议室中
                item = heapq.heappop(holds)
                if item[0] <= v[0]:
                    heapq.heappush(meets, [item[2], item[0], item[1]])
                else:
                    heapq.heappush(holds, item[:])
                    break
            met = None
            # 先从空闲会议室拿 否则从正在开会的拿
            if meets:
                met = heapq.heappop(meets)
                met = [met[1], met[2], met[0]]
            else:
                met = heapq.heappop(holds)
            # print(met)
            # else 后面表示的是推迟会议
            met[0], met[1] = v[1] if met[0] < v[0] else met[0] + v[1] - v[0], met[1] + 1
            # print(met)
            count = max(count, met[1])
            heapq.heappush(holds, met[:])

        while holds:
            item = heapq.heappop(holds)
            heapq.heappush(meets, [item[2], item[0], item[1]])
        for v in meets:
            if v[2] == count:
                ans = min(ans, v[0])
        return ans


from leetcode.tools import test_func_batch
ok="""
2
[[0,10],[1,5],[2,7],[3,4]]
3
[[1,20],[2,10],[3,5],[4,9],[6,8]]
"""
params = """
4
[[18,19],[3,12],[17,19],[2,13],[7,10]]
"""
test_func_batch(Solution().mostBooked, params)
