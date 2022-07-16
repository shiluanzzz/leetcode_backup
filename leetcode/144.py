# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 二叉数前序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = []
        result = []
        queue.append(root)

        while len(queue)!=0:
            node = queue.pop(0)
            result.append(node.val)

            if node.right: queue.insert(0,node.right)
            if node.left : queue.insert(0,node.left)

        return result