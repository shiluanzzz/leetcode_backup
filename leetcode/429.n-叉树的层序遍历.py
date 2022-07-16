#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=[]
        stack=[root]
        while stack:
            temp=[]
            lap=[]
            for each_node in stack:
                if each_node:
                    lap.append(each_node.val)
                    temp.extend(each_node.children)
            stack=temp
            if lap:
                ans.append(lap)
        return ans  
# @lc code=end

