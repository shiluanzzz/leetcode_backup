# 创建时间:2022-09-01 16:30:10


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # 本来是应该用约瑟夫环来解的，但是看不懂 用了一个双向指针来模拟
        # 构造一个环
        head = ListNode(1)
        p = head
        for i in range(2, n + 1):
            p.next = ListNode(i)
            p.next.prev = p
            p = p.next
        head.prev = p
        p.next = head  # 环连接起来

        # 还剩下超过1人时
        while n > 1:
            # while head.val != head.next.val:
            for _ in range(k - 1):
                head = head.next
            # print(head.val)
            p = head.next
            head.prev.next = head.next
            head.next.prev = head.prev
            head = p
            n -= 1
        return head.val


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    5
    2
    5
    1
    """
    from leetcode import tools

    tools.test_func_batch(Solution().findTheWinner, params)
