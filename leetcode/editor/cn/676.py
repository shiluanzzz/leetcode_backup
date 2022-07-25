#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#

# @lc code=start
from collections import defaultdict


class MagicDictionary:

    def __init__(self):
        self.hash = defaultdict(list)

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                t = list(word)
                t[i]="*"
                t = "".join(t)
                self.hash[t].append(word)

    def search1(self,origin,searchWord: str) -> bool:
        print(searchWord)
        t = self.hash[searchWord]
        if len(t) == 0:
            return False
        for each in t:
            if each!=origin:
                return True
        return False
    def search(self,word:str):
        for i in range(len(word)):
            t=list(word)
            t[i]="*"
            if self.search1(word,"".join(t)):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

a=MagicDictionary()
a.buildDict(["apple","hello"])
print(a.hash)
print(a.search("apple"))