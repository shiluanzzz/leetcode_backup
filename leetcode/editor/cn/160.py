# 160. 相交链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        q,p=headA,headB
        fq,fp=0,0
        while q!=p:
            if q.next:
                q=q.next
            elif not fq:
                fq=1
                q=headB
            else:
                return None
            if p.next:
                p=p.next
            elif not fp:
                p=headA
                fp=1
            else:
                return None
        return q

# leetcode submit region end(Prohibit modification and deletion)
