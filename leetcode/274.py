# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz


def solve(citations):
    # [3,0,6,1,5]
    citations.sort()
    n=len(citations)
    while n:
        if citations[-n] >= n:
            return n
        else:
            n-=1
    return n

a=solve([5,6,3,4,9])
print(a)