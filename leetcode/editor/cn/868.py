#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start 


class Solution:
    def binaryGap(self, n: int) -> int:
        ss=bin(n)[2:]
        if int('1'+'0'*(len(ss)-1),2)==n:return 0
        pre=ss.find('1')
        ans=0
        for i in range(pre+1,len(ss)):
            if ss[i]=='1':
                ans=max(ans,i-pre)
                pre=i
        return ans
# @lc code=end

print(Solution().binaryGap(321))