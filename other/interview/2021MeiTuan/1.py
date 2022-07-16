# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
# 围栏
def solve(n,m,h,l:list):
    # 不高于h，连续m个
    # l：list
    n=len(l)
    i,j=0,0
    while i < n and j<n:
        # print(i,j)
        if l[j]<=h:
            j+=1
            if j-i>=m:
                return i+1
        else:
            if j+m>n:
                return -1
            j+=1
            i=j
    return -1


if __name__ == '__main__':

    data1=map(int,input().strip().split())
    data2=map(int,input().strip().split())
    n,m,h=data1
    l=list(data2)
    print(solve(n, m, h, l))
    # n,m,h=5,5,2
    # print(solve(n,m,h,[1,1,1,2,2,3]))