

# 二叉树 的层序遍历

def solve(root):
    if root==None:
        return []
    res=[[root]]
    q=[root]
    while q:
        next_=[]
        while q:
            node=q.pop(0)
            if node.left != None:
                next_.append(node.left)
            if node.right != None:
                next_.append(node.right)
        res.append(next_)
        q=next_
    res.reverse()
    return res
