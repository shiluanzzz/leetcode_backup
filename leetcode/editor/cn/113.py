# 创建时间:2022-09-02 12:53:38


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []

        def dfs(node, target, path):
            if not node: return False
            target -= node.val
            path.append(node.val)
            if target == 0 and not node.left and not node.right:
                self.ans.append(path)
            return dfs(node.left, target, path[:]) or dfs(node.right, target, path[:])

        dfs(root, targetSum, [])
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

