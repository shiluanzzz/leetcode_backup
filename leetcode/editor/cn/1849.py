#
# @lc app=leetcode.cn id=1849 lang=python3
#
# [1849] 将字符串拆分为递减的连续值
#

# @lc code=start


class Solution:
    def splitString(self, s: str) -> bool:
        # review 关键词 枚举第一个数
        # 几个踩坑的点 ：200100
        # 剪枝的办法，往后面枚举的数比目标数都还大了就不用了，进
        # 函数的时候可以判断一下是否会出现200100这种情况
        def dfs(begin,target):
            if int(s[begin:])==target:
                return True
            if begin==len(s):
                return True
            if target<0:return False
            nums=""
            for i in range(begin,len(s)):
                nums+=s[i]
                if int(nums)==target:
                    return dfs(i+1,target-1)
                if int(nums)>target:
                    return False
            return False
        enum_first=""
        for i in range(len(s)-1):
            enum_first+=s[i]
            if dfs(i+1,int(enum_first)-1):
                return True
        return False
    
# @lc code=end
print(Solution().splitString("050043"))
print(Solution().splitString("90807060"))
print(Solution().splitString("10009998"))
print(Solution().splitString("050043"))
print(Solution().splitString("200100"))

