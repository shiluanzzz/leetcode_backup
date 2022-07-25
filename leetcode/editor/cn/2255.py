#
# @lc app=leetcode.cn id=2255 lang=python3
#
# [2255] 统计是给定字符串前缀的字符串数目
#

# @lc code=start
class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        ans = 0
        for i in words:
            if str(s).startswith(i):
                ans+=1
        return ans
# @lc code=end

