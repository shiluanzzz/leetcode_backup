# -*- coding:utf-8 -*-
# __author__ = "shitou6"
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3

def findLength(A:list,B:list)->int:

    max=0
    l=len(A) if len(A)>len(B) else len(B)
    for i in range(1,l+1):
        indexb=len(B)-i if len(B)-i>0 else 0
        each=findMaxLength(A[0:i if i<=len(A) else len(A)],
                           B[indexb:])
        max=each if each>max else max
    a=A
    b=B
    for i in range(1,l+1):
        indexb=len(a)-i if len(a)-i>0 else 0
        each=findMaxLength(b[0:i if i<=len(b) else len(b)],
                           a[indexb:])
        max=each if each>max else max
    print(max)
    return max


def findMaxLength(a,b):
    print("a:" + str(a))
    print("b:"+str(b))

    if a == b:
        return len(a)
    elif a in b:
        return len(a)
    elif b in a:
        return len(b)
    return 0

if __name__ == '__main__':
    findLength(
        [1,2,3,2,1,313,3,3,3,3,1,1,3,4,4,5,6,1,5,1,4,2,4,5,2,4,5,4,2,4],
        [3,2,1,4,7]
    )