# 创建时间:2022-09-02 12:27:45


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []

        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                self.ans.append("->".join(path[:]))
                return
            dfs(node.left, path[:])
            dfs(node.right, path[:])
        dfs(root,[])
        return self.ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

