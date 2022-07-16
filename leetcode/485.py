# -*- coding:utf-8 -*-
# __author__ = "shitou6"
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        # 没有考虑到数组[1] 的情况
        max_count=0
        count=0
        for i in nums:
            if i == 1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
        max_count=max(max_count,count)
        return max_count

S=Solution()
a=S.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(a)