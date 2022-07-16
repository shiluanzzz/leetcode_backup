# 面试题 16.10. 生存人数


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAliveYear(self, birth: list[int], death: list[int]) -> int:
        birth.sort()
        death.sort()
        print(birth,"\n",death)
        d=0
        ans,count=1989,0
        now_live=0
        for i in birth:
            while d<len(death) and death[d]<i:
                now_live-=1
                d+=1
            now_live+=1
            if now_live>count:
                ans,count=i,now_live
        return ans
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().maxAliveYear([1972,1908,1915,1957,1960,1948,1912,1903,1949,1977,1900,1957,1934,1929,1913,1902,1903,1901],
[1997,1932,1963,1997,1983,2000,1926,1962,1955,1997,1998,1989,1992,1975,1940,1903,1983,1969]))