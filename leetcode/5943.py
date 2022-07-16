# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q,p=head,head
        c=q
        flag=True
        while p!=None:
            if flag:
                p=p.next if p.next and p else None
                flag=False
            else:
                p = p.next if p.next and p else None
                p = p.next if p.next and p else None
                c=q
                q = q.next if q.next else None
                print(q.val)
        c.next=c.next.next
        return head
