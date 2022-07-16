#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
import collections
class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        if start==end:return 0
        bankset=set(bank)
        if end not in bankset:return -1
        q=collections.deque()
        q.append((start,0))
        while q:
            gene,count=q.popleft()
            for i,v in enumerate(gene):
               for newchar in "ACGT":
                    if v==newchar:continue
                    newG=gene[:i]+newchar+gene[i+1:]
                    # print(newG)
                    if newG in bankset:
                        if newG==end:
                            return count+1
                        else:
                            # print(q)
                            bankset.remove(newG)
                            q.append((newG,count+1))
        return -1
# @lc code=end
print(Solution().minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))