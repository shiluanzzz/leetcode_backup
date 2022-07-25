# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 交换两个数组元素使得两个数组相同。
# 只含有x,y字符.
def solve(s1,s2):
    i,j=len(s1),len(s2)
    if i!=j: return -1
    x1,x2=0,0
    y1,y2=0,0
    for k in range(i):
        if s1[k]!=s2[k]:
            if s1[k]=="x":
                y1+=1
                x2+=1
            else:
                y2+=1
                x1+=1
    print(x1,x2,y1,y2)
    if x1==y2 and y1==x2:
        return max(x1,y1)
    return -1

a=solve("xy","yx")
print(a)
a=solve(s1="xxyyxyxyxx", s2 = "xyyxyxxxyx")
print(a)
a=solve("xx","yy")
print(a)
