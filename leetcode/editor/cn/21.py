# -*- coding:utf-8 -*-
# __author__ = "shitou6"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # one is none
        if not( l1 and l2):
            return l1 if l1 else l2
        # all is none
        if l1 is None and l2 is None:
            return None
        begin=ListNode(0)
        p=begin
        while(l1 or l2):
            if l1.val<l2.val:
                p.next=ListNode(l1.val)
                p=p.next
                l1=l1.next if l1.next else None
            else:
                p.next=ListNode(l2.val)
                p=p.next
                l2=l2.next if l2.next else None
            if l1 is None:
                p.next=l2
                break
            if l2 is None:
                p.next=l1
                break
        return begin.next
    def mergeTwoLists2(self,l1:ListNode,l2:ListNode) -> ListNode:
        # end
        if not l1 : return  l2
        if not l2 : return  l1
        # other
        if l1.val < l2.val:
            l1.next=self.mergeTwoLists2(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists2(l1,l2.next)
            return l2