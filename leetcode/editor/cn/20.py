# -*- coding:utf-8 -*-
# __author__ = "shitou6"
import queue


class Solution:
    def isValid(self, s: str) -> bool:
        q=[]
        while len(s):
            if len(q) and self._equal(q[0],s[:1]):
                q.pop(0)
                q=self.check(q)
            else:
                q.append(s[:1])
            s=s[1:]
        print(q)
        return False if len(q) else True

    def check(self,q:list):
        if len(q)==0:
            return q
        if len(q)%2==0 and self._equal(q[0],q[-1]):
            q.pop(0)
            q.pop(len(q)-1)
            return self.check(q)
        else:
            return q

    def _equal(self,x,y):
            if x is "(" and y is ")" or x is ')' and y is '(':
                return True

            if x is "{" and y is "}" or x is '}' and y is '{':
                return True

            if x is "[" and y is "]" or x is ']' and y is '[':
                return True


# 求最小括号对
class Solution2:
    def isValid(self, s: str) -> bool:
        q=[]
        while len(s):
            if len(q) and self._equal(q[-1],s[:1]):
                q.pop(-1)
                # q=self.check(q)
            else:
                q.append(s[:1])
            s=s[1:]
        print(q)
        return False if len(q) else True

    def _equal(self,x,y):
        if x is "(" and y is ")" or x is ')' and y is '(':
            return True

        if x is "{" and y is "}" or x is '}' and y is '{':
            return True

        if x is "[" and y is "]" or x is ']' and y is '[':
            return True


class Solution3:
    def isValid(self, s: str) -> bool:
        dic={'}':'{',')':'(',']':'['}
        stack=[]
        for i in s:
            if stack and i in dic: # 栈非空，且i为右括号才有可能匹配
                if stack[-1]==dic[i]:
                    stack.pop(-1)
                else: return False # 这里没考虑到，如果有右括号没匹配到哪肯定就不能结束
            else:
                stack.append(i)
        return False if stack else True

a=Solution3()
# print(a.isValid("()[]{}"))
print(a.isValid("{[]}"))

