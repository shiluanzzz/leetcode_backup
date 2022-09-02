# 创建时间:2022-09-02 18:47:52


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node) -> int:
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

    tools.test_func_batch(Solution()., params)
