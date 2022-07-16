# 1705. 吃苹果的最大数目


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        app ,ans,now= [],0,0
        # 当可以摘苹果或者有苹果可以吃的时候 就继续过一天
        while now < len(apples) or len(app):
            # 摘苹果放入最下堆中
            if now < len(apples): heapq.heappush(app, [now + days[now]-1, apples[now]])
            # 当堆里的苹果已经要坏掉了或者吃完了
            while len(app) and (app[0][0] < now or app[0][1] < 1):
                heapq.heappop(app)
            # 吃苹果
            if len(app):
                app[0][1] -= 1
                ans += 1
            now += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().eatenApples([1,2,3,5,2], [3,2,1,4,2]))
