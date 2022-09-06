# 110. 平衡二叉树

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def dfs(node):
            if not self.ans: return 0
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(right - left) > 1: self.ans = False
            return max(left, right) + 1

        dfs(root)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

    # tools.test_func_batch(Solution()., params)
