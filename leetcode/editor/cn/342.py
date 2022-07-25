# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

#判断是否是4的幂次方
# 循环查找
def func(n):
    if n == 0 :return False
    # 一开始忘了0这个特殊输入了。
    ans=0
    while n%4==0:
        n=n//4
        ans+=1
    # print(ans)
    return True if n ==1  else False

def func2(n):
    if n == 0 :return False
    left = 0
    right = 15
    while left <= right:
        mid = (left+right)//2
        if pow(4,mid) == n:
            return True
        if pow(4,mid) < n:
            left = mid+1
        if pow(4,mid) > n:
            right = mid-1
    return False



a=func2(43525235)
print(a)