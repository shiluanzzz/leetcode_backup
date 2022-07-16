# 1154. 一年中的第几天


# leetcode submit region begin(Prohibit modification and deletion)
import time


class Solution:
    def dayOfYear(self, date: str) -> int:
        print(list(time.strptime(date,"%Y-%m-%d")))
        return time.strptime(date, "%Y-%m-%d")[-2]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().dayOfYear("1992-05-21")