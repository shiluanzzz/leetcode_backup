# 创建时间:2022-09-02 13:04:24


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "~"

        # 面向解析做的
        def dfs(node, path: list):
            if not node: return
            path.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                self.ans = min(self.ans, "".join(path))

            dfs(node.left, path)
            dfs(node.right, path)
            # 因为要dfs其他路径，所以最后需要pop
            path.pop()

        dfs(root, [])
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
