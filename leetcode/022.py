# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


def solve(n):
    l,r=n,n
    res=[]

    def gen(l,r,ans):
        if l==r and l==0:
            res.append(ans)
            return ;
        if ans=="":
            gen(l-1,r,"(")
            return ;
        if l==0:
            res.append(ans+")"*r)
            return ;
        else:
            if l>0:
                gen(l-1,r,ans+"(")
            if r>0 and r>l:
                gen(l,r-1,ans+")")

    gen(n,n,"")
    return res

print(solve(8))