# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 三数之和

def solve(nums:list):
    res=[]
    nums.sort()
    for index,i in enumerate(nums):
        for kindex,k in enumerate(nums[index+1:]):
            for qindex ,q in enumerate(nums[kindex+1:]):
                if i+k+q==0:
                    res.append([i,k,q])
                if i+k+q>0:
                    break
                else:
                    continue
    return res
print(solve([-1,0,1,2,-1,-4]))
