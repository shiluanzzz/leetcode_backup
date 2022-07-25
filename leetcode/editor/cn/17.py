# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

def solve(digits):
    if digits=="":
        return []
    key=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    res=[i for i in key[int(digits[0])]]

    for each in digits[1:]:
        t=[]
        for i in key[int(each)]:
            for k in res:
                t.append(k+i)
        res=t.copy()
    return res
def solve2(digits):
    key=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    # 回溯
    ans=[]
    def d(res,next):
        a=[]
        if len(next)!=0:
            for each in key[int(next[0])]:
                a.extend(d(res+each,next[1:]))
            return a
        else:
            return [res]

    return d("",digits)



print(solve2("2343"))
