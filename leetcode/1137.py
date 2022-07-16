# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


def solve(n):
    k={
        0:0,1:1,2:1
    }
    def tb(n):
        r=k.get(n)
        if r!=None:
            return r
        else:
            r=tb(n-3)+tb(n-2)+tb(n-1)
            k[n]=r
            k.pop(n-3)
            return r
    return tb(n)

def solve2(n):
    k={
        0:0,1:1,2:1
    }
    for i in range(n+1):
        if i in [0,1,2]:
            continue
        k[i]=k[i-3]+k[i-2]+k[i-1]
    return k[n]

a=solve2(25)
print(a)