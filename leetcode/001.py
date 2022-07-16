# -*- coding:utf-8 -*-
# __author__ = "shitou6"

def two_sum(nums,target):
    for x in nums:
        y=target-x
        if y in nums:
            if nums.index(x)==nums.index(y):
                continue
            else:
                return [nums.index(x),nums.index(y)]
        else:
            continue #当两个数字相同时，在下一次循环，就不会取到相同的index！

#为什么不直接遍历nums，因为这样第二次取index时依然时一样的。
#先从index里取的话 等第二次遍历到相同时，y为第一个，x为第二个
def s2(nums,target):
    n = len(nums)
    for x in range(n):
        a=target-nums[x]
        if a in nums:
            y=nums.index(a)
            if x != y:
                return [x,y] if x<y else [y,x]
        else:
            continue
print(s2([1,1],2))

def s3_review(nums,target):
    n=len(nums)
    for i in range(n):
        j=i+1
        while j<n:
            if nums[i]+nums[j]==target:
                return [i,j]
            else:
                j+=1
print(s3_review([3,2,1,3,1],4))