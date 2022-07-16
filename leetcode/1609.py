

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        nodes=[root]
        def dfs(nodes,depth):
            new_nodes=[]
            for i,v in enumerate(nodes):
                if i!=0 and nodes[i].val>nodes[i-1].val != depth%2==0:
                    return False
                if v.val%2==0 != depth%2==0:
                    return False
                if v.left:new_nodes.append(v.left)
                if v.right:new_nodes.append(v.right)
            if new_nodes==[]:return True
            return dfs(new_nodes,depth+1)
        return dfs(nodes,0)
if __name__ == '__main__':