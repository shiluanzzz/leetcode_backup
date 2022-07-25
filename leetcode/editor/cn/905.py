# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


# 数组奇偶排序， 偶数在前奇数在后。

def solve(A:list):
    n=len(A)
    if not n: return []
    for i in range(n):
        print(A[i],end=" ")
        if A[i]%2==0:
           A.insert(0,A.pop(i))
        i+=1
    return A


a=solve([1,2,3,4,1,3,4,1,5,36,6,3,5,1,1,5,4,2,4,2])
print(a)
