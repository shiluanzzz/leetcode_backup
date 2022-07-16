# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
import random

def solve1(nums):
    flag=[0]*len(nums)
    flag[0]=1

    def solve(nums,begin):
        if len(nums)==1 and nums[0]>=0:
            return True
        if nums[0]>=len(nums):
            return True
        else:
            for i in range(1,nums[0]+1):

                if solve(nums[i:],begin+i):
                    return True
        return False
def solve2(nums):
    n=len(nums)
    # if n==1:return True
    flag = [0]*n
    flag[0]=1
    for index,item in enumerate(nums):
        if index+item+1>=n and flag[index]==1:
            return True
        elif flag[index]==1:
            flag[index+1:index+item+1]=[1]*item
        else:
            continue
    return False
def solve3(nums):

    m=0
    for i in range(len(nums)):
        if i>m:
            return False
        m=max(m,i+nums[i])

    # if m>=len(nums):
    return True

def gen():
    for i in range(10):
        a=[]
        n=random.randint(5,20)
        for k in range(n):
            a.append(random.randint(0,n-3))
        print(a)
if __name__ == '__main__':
    # gen()
    print("123test")
    print(solve3([2,3,1,1,4]))
    print(solve3([3,2,1,0,4]))
    print(solve3([4,2,3,4,1,1,4,2,4,5,23,4,2,4,4,5,2]))
    print(solve3([4,3,2,4,1,4,2,4,3,1,1,0,3]))
    print(solve3([1,1,1,1,1]))
    print(solve3([0]))
    print(solve3([2,0,0]))
    print(solve3([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))

