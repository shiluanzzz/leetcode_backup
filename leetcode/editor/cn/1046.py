# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
import heapq


def lastStoneWeight(stones) -> int:

    def insert_into(l,item):
        for index ,i in enumerate(l):
            if item <=i:
                return l[:index]+[item]+l[index:]
        return l+[item]
    def func1(x,y):

        return y-x

    stones.sort()
    while len(stones) >= 2:
        item = func1(stones.pop(-2),stones.pop(-1))
        if item!=0:
            stones=insert_into(stones,item)

    if len(stones) == 1: return stones[0]
    if len(stones) == 0: return 0

def func2(nums):
    nums=[-i for i in nums]
    heapq.heapify(nums)
    while len(nums)>1:
        x,y=heapq.heappop(nums),heapq.heappop(nums)
        print(nums)
        print(x,y)
        if x!=y:
            heapq.heappush(nums,x-y)
    if nums: return -nums[0]
    return 0


print(func2([2,3,1,4,1,5,1,3]))
