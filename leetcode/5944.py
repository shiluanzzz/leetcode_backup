# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        path=[]
        def findNode(root,target):
            if not root:
                return False
            if root.val==target:
                return True

            path.append("R")
            if findNode(root.right,target):
                return True
            path.pop()
            path.append("L")
            if not findNode(root.left,target):
                path.pop()
                return False
        findNode(root,startValue)
        start=path.copy()
        path=[]
        findNode(root,destValue)
        end=path
        maxd=0
        for i in range(min(len(start),len(end))):
            if start[i]==end[i]:
                maxd+=1
            else:
                break
        print(end)
        start=start[maxd:]
        end=end[maxd:]
        return "U"*len(start)+"".join(end)

