# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 数组按位异或

def solve(n,start):
    i=1
    result=start
    while i<n:
        result=result^(start+2*i)
        i+=1
    return result

a=solve(10,5)
print(a)