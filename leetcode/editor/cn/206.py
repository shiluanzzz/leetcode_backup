# 创建时间:2022-09-01 15:54:28


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList1(self, head: [ListNode]) -> [ListNode]:
        if not head or not head.next:
            return head
        # 迭代的方式反转链表
        p = None
        while head.next:
            q = head.next
            head.next = p
            p = head
            head = q
        head.next = p
        return head

    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # 这个递归还要多理解
        if not head or not head.next:
            return head
        let = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return let


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

