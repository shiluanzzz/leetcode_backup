# 创建时间:2022-09-02 12:49:52


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target):
            if not node: return False
            target -= node.val
            if target == 0 and not node.left and not node.right: return True
            return dfs(node.left, target) or dfs(node.right, target)

        return dfs(root, targetSum)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
