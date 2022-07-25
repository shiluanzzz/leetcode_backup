# -*- coding:utf-8 -*-
# __author__ = "shitou6"

class Solution:
    def longestCommonPrefix(self, strs:list) -> str:
        # 输入: ["flower","flow","flight"]
        # 输出: "fl"
        ans=""
        for i in zip(*strs):
            if len(set(i))==1:
                ans+=i[0]
            else:
                break
        return ans
