# 187. 重复的DNA序列


# leetcode submit region begin(Prohibit modification and deletion)
import collections

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        count=collections.defaultdict(int)
        ans=[]
        for i in range(len(s)-10):
            count[s[i:i+10]]+=1
            if count[s[i:i+10]]==2:
                ans.append(s[i:i+10])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
