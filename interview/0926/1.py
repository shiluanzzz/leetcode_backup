

class TreeNode:
    def __init__(self,val:int):
        self.val=val
        self.left=None
        self.right=None

def printTreeByRight(head:TreeNode)->list:
    if not head:
        return []
    queue=[head]
    res=[]
    while queue:
        res.append(queue[-1].val)
        temp=[]
        for node in queue:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue=temp
    print(res)

if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(4)
    printTreeByRight(root)