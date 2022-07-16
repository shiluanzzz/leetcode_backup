# 539. 最小时间差


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        time=[int(i[:2])*60+int(i[-2:]) for i in timePoints]
        time.sort()
        ans=time[0]-time[-1]+24*60
        for i,v in enumerate(time[1:],1):
            ans=min(abs(time[i-1]-time[i]),ans)
        return ans
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a=Solution().findMinDifference([
        "00:00","23:59","00:00"
    ])
    print(a)