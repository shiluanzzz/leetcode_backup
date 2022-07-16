# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


def solve(arr):
    s=set(arr)

    for i in s:
        if 2*i in s and i!=0:
            return True
        if i==0 and arr.count(i)>=2:
            return True
    return False

a=solve([-2,0,10,-19,4,6,-8])
print(a)