#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

from this import d
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # TODO 只想到了把链表转化为数字 ，然后累加后在转化回去
        num1=0
        while l1:
            num1= num1+l1.val if l1.next==None else (num1+l1.val)*10
            l1=l1.next
        num2=0
        while l2:
            num2= num2+l2.val if l2.next==None else (num2+l2.val)*10
            l2=l2.next
        res=num1+num2
        # print(num1,num2,res)

        l3=[int(i) for i in list(str(res))]
        # print(l3)
        p=ListNode(0)
        ans=p
        for i in l3:
            p.next=ListNode(i)
            p=p.next
        return ans.next
# @lc code=end

