# -*- coding:utf-8 -*-
# __author__ = "shitou6"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = result = ListNode(None)
        s = 0  # 暂存和 防止有和》10的情况
        while l1 or l2 or s:
            s = s + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            result.next = ListNode(s % 10)
            result = result.next
            s //= 10  # 进位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None  # 这里也要判断，不判断的话 none 是 没有next的
        return p.next

    # 比较完美的写法，使用while循环，如果链表为空就直接给默认值0，最后记得检查op
    # 链表取next和val的时候需要检查指针是否为空
    # 在激进一点的写法就可以像上面的那样
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(0)
        result = r
        op = 0
        while (l1 or l2):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            num = op + a + b
            op = num // 10
            result.next = ListNode(num % 10)
            result = result.next
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        if op:
            result.next = ListNode(1)
        return r.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = self.getNumbers(l1) + self.getNumbers(l2)
        result = ListNode(r % 10)
        r = r // 10
        while not r is 0:
            result.next = ListNode(r % 10)
            r = r // 10
        return result

    def getNumbers(self, l1: ListNode):
        a = 0
        c = 1
        while (1):
            a += l1.val * c
            c *= 10
            if not l1.next:
                break
            l1 = l1.next
        return a
