# -*- coding:utf-8 -*-
# __author__ = "shitou6"
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 遍历一遍，并把所有的节点放在数组中？
        len=1
        node_list=[]
        while(head.next):
            len+=1
            node_list.append(head)
            head=head.next
        node_list.append(head)
        return node_list[-k]

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        # 双指针
        q=head
        p=head
        while(k):
            k-=1
            p=p.next # 根据题意不需要进行边界操作
        while p:
            q,p=q.next,p.next
        return q

def new_Node(data:list)->ListNode:
    head=ListNode(0)
    d=head
    for i in data:
        t=ListNode(i)
        d.next=t
        d=d.next
    return head.next
def print_Node(node:ListNode):
    while node.next:
        print(node.val,end=" , ")
        node=node.next
    print(node.val,end=" , ")

if __name__ == '__main__':
    S=Solution()
    print_Node(S.getKthFromEnd2(new_Node([1,2,3,4,5]),2))

