# -*- coding:utf-8 -*-
# __author__ = "shitou6"
# 判断回文数
def isPalindrome(x: int) -> bool:
    stack=[]
    t=x
    while x:
        stack.append(x%10)
        x=x//10
    new=0
    while stack:
        c=stack.pop(0)
        new+=c
        new*=10
    new=new//10
    if new == t:
        return True
    else:
        return False
def ex2(x:int)->bool:
    if x<0:
        return False
    if x<10:
        return True
    if x%10==0:
        return False
    stack = []
    t = x
    while x:
        stack.append(x % 10)
        x = x // 10
    i=0
    j=len(stack)-1
    while i<j:
        if stack[i]!=stack[j]:
            return False
        i+=1
        j-=1
    return True

def ex3(x:int):
    s=str(x)
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True



if __name__ == '__main__':
    print(ex3(12345))
    print(ex3(12321))
    print(ex3(1111))
    print(ex3(22222))
    print(ex3(1230))
    print(ex3(65665))
