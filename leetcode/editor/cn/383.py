#
# @lc app=leetcode.cn id=383 lang=python3
# @ 20220830
# [383] 赎金信
#

# @lc code=start
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        for k in c1.keys():
            if c2[k] < c1[k]:
                return False
        return True

    def canConstruct_history(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = {}
        for i in magazine:
            mag.setdefault(i, 0)
            mag[i] += 1
        for i in ransomNote:
            mag.setdefault(i, 0)
            mag[i] -= 1
            if mag[i] < 0:
                return False
        return True
# @lc code=end
