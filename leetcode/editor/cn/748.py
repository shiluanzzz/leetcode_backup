# 748. 最短补全词


# leetcode submit region begin(Prohibit modification and deletion)
import re
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        res=re.findall('[a-zA-Z]+',licensePlate)
        key="".join(res)
        key=key.lower()
        print(key)
        hash={}
        for v in key:
            hash[v]+=1

        for each in words:

        return ""
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a="aA"
    b=a.lower()
    b="b"
    print(a,b)