# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
import heapq


def mypow(x,n):
    flag=0
    if n<0:
        n=-n
        flag=1
    res=1
    ace_record=[]

    while n>1:
        f=False
        if len(ace_record)==0:
            heapq.heappush(ace_record,[2,x*x])
            res*=(x*x)
            n-=2
            continue

        for i in ace_record[::-1]:
            if i[0]*2<n:
                t=(i[1]*i[1])
                n=n-i[0]*2
                res*=t
                heapq.heappush(ace_record,[i[0]*2,t])
                f=True
        if not f:
            res*=x
            n-=1


    if n==0 and flag==1: return 1/res
    if n==0 and flag==0: return res
    if n==1 and flag==1: return 1/(res*x)
    else:
        return res*x


print(mypow(2.0000,0))
for i in [3,2,4,5,6,-3,-4,-6]:
    assert mypow(2,i)==pow(2,i)