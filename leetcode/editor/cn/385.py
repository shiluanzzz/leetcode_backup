#
# @lc app=leetcode.cn id=385 lang=python3
#
# [385] 迷你语法分析器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from os import defpath


class Solution:
    def deserialize(self, s: str):
        if s[0]!="[":return int(s)
        ans=[]
        stack=[]
        num=""
        for i in s[1:-1]:
            if i=='[':
                stack.append([])
            elif i==']':
                ans.append(stack.pop())
            elif i==',':
                num=int(num)
                if len(stack):
                    stack[-1].append(num)
                else:
                    ans.append(num)
                num=""
            else:
                num+=i
        return ans
# @lc code=end

print(Solution().deserialize("[123,[456,[789]],898,[1]]"))