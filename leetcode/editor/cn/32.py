#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        self.ans=0
        self.count_left=0
        # 记录合法子串的开始位置
        self.t=0
        def op(i,value):
            # "()(()"
            if value==")":
                if self.count_left>0:
                    self.count_left-=1
                    self.t+=2
                else:
                    # 当出现一个多余的右括号的时候就要重新计算了
                    self.ans=max(i-self.t,self.ans)
                    self.t=i+1
            else:
                self.count_left+=1
        for i,v in enumerate(s):
            op(i,v)
        return max(self.ans,self.t)
# @lc code=end

print(Solution().longestValidParentheses(")()())"))
