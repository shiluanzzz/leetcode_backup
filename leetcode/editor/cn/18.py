# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

def solve(nums:list,target):
    if len(nums)<4:return []
    res=[]
    n=len(nums)
    nums.sort()
    i=0

    while i<n-1:
        q,p=0,n-1
        while q<p:
            if q==i or q==i+1:
                q+=1
                continue
            if p==i or p==i+1:
                p-=1
                continue
            t=nums[i]+nums[i+1]+nums[q]+nums[p]
            if t==target:
                r=sorted([nums[i],nums[i+1],nums[q],nums[p]])
                if r not in res:
                    res.append(r)
            if t>0:
                p-=1
            else:
                q+=1
        i+=1
    return res

if __name__ == '__main__':
    # print(solve([2,2,2,2,2],8))
    print(solve([-3,-2,-1,0,0,1,2,3],0))