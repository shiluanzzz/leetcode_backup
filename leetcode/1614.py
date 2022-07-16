# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

def solve(s):
    result=0
    z,y=0,0
    for i in s:
        if i=='(':
            z+=1
            result=max(result,z)
        elif i==")":
            z-=1
        else:
            continue
    return result

