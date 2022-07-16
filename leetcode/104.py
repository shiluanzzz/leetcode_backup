# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"



# Definition for a binary tree node.
import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root:TreeNode) -> int:
        if not root:
            return 0

        q=queue.Queue()
        q.put(root)
        depth=0
        while(not q.empty()):
            size=q.qsize()
            for i in range(size):
                temp=q.get()
                if not temp:
                    break
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
            depth+=1
        return depth

