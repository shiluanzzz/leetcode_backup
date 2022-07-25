# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


# 二进制反码对应的数



def solve(N):

    b = bin(N)
    s=""
    for i in b[2:]:
        if i == "0":
            s+="1"
        else:
            s+="0"

    # fan = int(b[2:]) ^ int("1" * len(str(b)))
    return int(s,2)

a=solve(111)
print(a)
