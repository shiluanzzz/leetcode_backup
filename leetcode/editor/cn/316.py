#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
import collections
from string import printable


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt=collections.Counter(s)
        ans=[]
        for i in s:
            if i not in ans:
                while len(ans) and ans[-1]>i and cnt[ans[-1]]>0:
                    ans.pop()
                ans.append(i)
            cnt[i]-=1
        return "".join(ans)
# @lc code=end

a=Solution().removeDuplicateLetters("bcabc")
print(a)