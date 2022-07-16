# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def InitTree(nums:list):
    if len(nums) == 0: return None
    # 取根节点
    root = TreeNode(nums.pop(0))
    q = queue.Queue()
    q.put(root)
    #
    while nums:
        begin = q.get()
        # 取根节点 放左右节点
        begin.left=TreeNode(nums.pop(0))
        q.put(begin.left)
        if nums:
            begin.right=TreeNode(nums.pop(0))
            q.put(begin.right)
    return root

def PrintTree(root:TreeNode):
    if not root:return
    nums=[]
    nums.append(root.val)


if __name__ == '__main__':
    a=InitTree([1,2,None,3,4,5])
    print(a)




