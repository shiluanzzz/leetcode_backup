#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

from operator import le


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:return 0
        ans=0
        ll=[root]
        while ll:
            temp=ll.pop(0)
            ans+=1
            if temp.left:ll.append(temp.left)
            if temp.right:ll.append(temp.right)
        return ans
    # TODO 解法2 利用完全二叉树的特性+二分查找
# @lc code=end

