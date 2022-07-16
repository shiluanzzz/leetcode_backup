# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

def solve(nums):
    n=len(nums)
    m=0
    for i in range(n-1,-1,-1):
        #往前找一个比自己小的数字换位置
        if nums[i]<m: continue
        k=i-1
        while k>=0:
            if nums[i]>nums[k]:
                t=nums[i]
                nums.remove(nums[i])
                nums.insert(k,t)
                return nums
            else:
                k-=1
        if k==0:
            m=max(m,k)
    nums.reverse()
    return nums

print(solve([2,3,1]))