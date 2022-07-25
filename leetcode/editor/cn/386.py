#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans=[0]*n
        ans[0]=1
        prev = 1
        for i in range(1,n):
            if prev*10<=n:
                prev*=10
                ans[i]=prev
            else:
                while prev%10==9 or prev+1>n:
                    prev//=10
                prev+=1
                ans[i]=prev
        return ans
                        
# @lc code=end


print(Solution().lexicalOrder(13))
print(Solution().lexicalOrder(130))