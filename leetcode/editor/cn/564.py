# 564. 寻找最近的回文数


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n=[i for i in n]
        q,p=0,len(n)-1
        while q<p:
            if n[q]!=n[p]:
                n[p]=n[q]
            q,p=q+1,p-1

        return "".join(n)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().nearestPalindromic("1233144312"))