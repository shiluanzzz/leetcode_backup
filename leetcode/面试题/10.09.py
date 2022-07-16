# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。


def solve2(nums,target):
    if len(nums)==0 or len(nums[0])==0 : return  False
    if nums[0][0]>target: return  False
    max_l=len(nums[0])
    for i in nums:
        for j in i[:max_l]:
            print(j,max_l)
            if j>target: max_l=min(max_l,i.index(j))
            if j==target: return True
    return False

def solve3(nums,target):
    if len(nums)==0 or len(nums[0])==0 : return  False
    if nums[0][0]>target: return  False
    col,row = 0,0
    while col <len(nums) and row <len(nums[0]) and col>0 and row >0:
        if nums[col][row]>target:
            col+=1

        if nums[col][row]==target:
            return True
        else:
            row+=1


a=solve2(
    [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ],5
)
print(a)