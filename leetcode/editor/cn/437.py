# 创建时间:2022-09-02 12:56:35


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def nodeSum(node, sum):
            if not node: return 0
            sum -= node.val
            ans = 1 if sum == 0 else 0
            return ans + nodeSum(node.left, sum) + nodeSum(node.right, sum)

        def pathSum(node, sum):
            if not node: return 0
            return nodeSum(node, sum) + pathSum(node.left, sum) + pathSum(node.right, sum)

        return pathSum(root, targetSum)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
