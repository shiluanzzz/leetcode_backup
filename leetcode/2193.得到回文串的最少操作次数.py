#
# @lc app=leetcode.cn id=2193 lang=python3
#
# [2193] 得到回文串的最少操作次数
#

# @lc code=start
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # 从最左边找一个数，如果对应到右边不是回文，找一个最近的字符交换过去
        # 转化为子问题
        s=[i for i in s]
        ans=0
        n=len(s)
        i,j=0,len(s)-1
        while i<j:
            if s[i]==s[j]:
                i,j=i+1,j-1
            else:
                flag=True
                for k in range(j,i,-1):
                    if s[k]==s[i]:
                        # k<->j
                        print(k,"<->",j)
                        while k<j:
                            s[k],s[k+1]=s[k+1],s[k]
                            ans+=1
                            k+=1
                        flag=False
                        break
                if flag:
                    # 单个字符 交换到中间
                    print(i,"<->",n//2)
                    for k in range(i,n//2):
                        s[k],s[k+1]=s[k+1],s[k]
                        ans+=1
                else:
                    i,j=i+1,j-1
        print("".join(s))
        return ans
# @lc code=end

print(Solution().minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii"))