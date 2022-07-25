# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 按频率将数组升序排序
# 转元组取个数。

def func(nums):
    # single=set(nums)
    nums_dict={}
    for each in nums:
        nums_dict.setdefault(each,0)
        nums_dict[each]+=1

    nums_dict=sorted(nums_dict.items(),key=lambda x:(x[1],-x[0]))
    ans=[]
    for k,v in nums_dict:
        ans.extend([k]*v)
    return ans

func([1,4,3,3,4,2,3,4,5,6,1])