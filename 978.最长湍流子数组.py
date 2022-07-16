#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#

# @lc code=start
from hashlib import new


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if len(arr)<2:
            return len(arr)
        op=-1
        lens=1
        ans=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                op=-1
                lens=1
                continue
            if op==-1:
                lens+=1
                op=1 if arr[i]>arr[i-1] else 0
            else:
                new_op=1 if arr[i]>arr[i-1] else 0
                if new_op+op==1:
                    op=new_op
                    lens+=1
                else:
                    # 同号
                    lens=2
                    op=new_op
            ans=max(lens,ans)
        return ans
# @lc code=end

print(Solution().maxTurbulenceSize([9,9]))