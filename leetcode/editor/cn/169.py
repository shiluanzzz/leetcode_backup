# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
import math


def solve(nums):
    target = math.floor(len(nums)/2)

    j  = {} # count:item
    max_count=0
    for i in nums:
        j.setdefault(i,0)
        j[i]+=1
    for k,v in j.items():
        if v>target:
            return k


a=solve([2,2,2,1,1,1,3])
print(a)