# 83. 删除排序链表中的重复元素

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        p = head
        while p and p.next:
            if p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return head
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    # from leetcode import tools
    #
    # tools.test_func_batch(Solution()., params)
