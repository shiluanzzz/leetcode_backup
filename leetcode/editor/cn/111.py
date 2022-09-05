# 111. 二叉树的最小深度

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node,depth):
            if not node.left and not node.right:
                return depth
            # TODO 应该还可以优化一下
            left=dfs(node.left,depth+1) if node.left else float('inf')
            right=dfs(node.right,depth+1) if node.right else float('inf')
            return min(left,right)
        return dfs(root,1)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

    # tools.test_func_batch(Solution()., params)
