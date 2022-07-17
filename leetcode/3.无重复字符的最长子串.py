#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        c=collections.defaultdict(int)
        temp_ans=0
        repead_char_idx=0
        for i,v in enumerate(s,1):
            if v in c and c[v]>=repead_char_idx:
                ans=max(ans,temp_ans)
                temp_ans=i-c[v]
                # 当有重复字符的时候，重复字符前面的全废了
                repead_char_idx=c[v]
                c[v]=i
            else:
                temp_ans+=1
                c[v]=i
        return max(ans,temp_ans)
# @lc code=end

print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("a*&cabdd"))
print(Solution().lengthOfLongestSubstring("bbbbbbbb"))
print(Solution().lengthOfLongestSubstring("bb clz77bbb"))