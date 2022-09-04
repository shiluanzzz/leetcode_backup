# 创建时间:2022-09-01 10:09:06


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 没有注意空指针的问题
        if head == None: return head
        n = 0
        p = head
        while p != None:
            p = p.next
            n += 1
        if k % n == 0: return head
        p = head
        for i in range(n - k % n - 1):
            p = p.next
        ans = p.next
        p.next = None
        # 这里，ans可能就是最后一个元素，所以需要判断
        if ans.next == None:
            ans.next = head
            return ans
        # p有可能是None
        p = ans.next
        while p and p.next != None:
            p = p.next
        p.next = head
        return ans


# leetcode submit region end(Prohibit modification and deletion)


