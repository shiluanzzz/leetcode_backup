# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

def solve(s)->int:
    keyd={1:"A"} #"a chr 97"
    for i in range(1,27):
        keyd[i]=chr(64+i)
    # print(keyd)
    n=len(s)
    i=0
    result=0
    while i<n:
        k=i+1
        while k<=n:
            if int(s[i:k]) in keyd.keys():
                result+=1
                print(s[i:k])
                k+=1
            else:
                break
        i=k-1
    return result

a=solve("226")
print(a)