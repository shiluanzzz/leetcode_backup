# -*- coding:utf-8 -*-
# __author__ = "shitou6"

class Solution:
    def removeDuplicates(self, nums) -> int:

        lens=len(nums)
        q=0
        p=q+1
        while(p<lens):
            if nums[q]==nums[p]:
                p+=1
            else:
                nums[q+1]=nums[p]
                q+=1
                p+=1

        print(nums)
        nums=nums[:q+1]
        print(nums)
        return q+1

class Solution2:
    def removeDuplicates(self, nums) -> int:
        lens=len(nums)
        q=0 # 未重复
        p=q+1 # 待检验
        while(p<lens):
            if(nums[q]==nums[p]):
                p=p+1
            else:
                nums[q+1]=nums[p]
                q+=1
                p+=1

        nums=nums[:q+1]
        print(nums)
        return q+1
if __name__ == '__main__':
    k=Solution2()
    a=k.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(a)
