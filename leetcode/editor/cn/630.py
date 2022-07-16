# 630. 课程表 III


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        # 按照课程的结束时间升序
        courses=sorted(courses,key=lambda x:(x[1],x[0]))
        print(courses)
        total=0 # 当前课程的结束时间
        heap=[]
        for d,l in courses:
            if d+total<=l:
                total+=d
                # 当前课程没有超时，入堆，堆顶是课程持续时间最长的课，因此放入-d
                heapq.heappush(heap,-d)
            elif heap and d<-heap[0]:
                # 如果堆中的有课程耗时比这个还长就替换这两个课程
                total+=heapq.heappop(heap)
                total+=d
                heapq.heappush(heap,-d)
        return len(heap)

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().scheduleCourse(
[[100,200],[200,1300],[1000,1250],[2000,3200]])