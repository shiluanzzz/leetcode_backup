# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。 
# 
#  请你返回字符串的能量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "leetcode"
# 输出：2
# 解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
#  
# 
#  示例 2： 
# 
#  输入：s = "abbcccddddeeeeedcba"
# 输出：5
# 解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
#  
# 
#  示例 3： 
# 
#  输入：s = "triplepillooooow"
# 输出：5
#  
# 
#  示例 4： 
# 
#  输入：s = "hooraaaaaaaaaaay"
# 输出：11
#  
# 
#  示例 5： 
# 
#  输入：s = "tourist"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母。 
#  
#  Related Topics 字符串 👍 68 👎 0

import groupby
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        char,count=s[0],1
        ans=1
        for item in s[1:]:
            if item==char:
                count+=1
            else:
                ans=max(ans,count)
                char,count=item,1
        ans=max(ans,count)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s="hourrrraaayy"
    print(groupby(s))