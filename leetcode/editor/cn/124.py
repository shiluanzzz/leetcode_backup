# 创建时间:2022-09-02 15:39:15


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum1(self, root: Optional[TreeNode]) -> int:
        # ok解法
        # 拆分这个问题就是分别找出左子树的最长路径和右子树的最长路径
        # 而子树的左右最长路径又可以继续拆分,因此用递归做
        self.ans = -float('inf')

        def dfs(node) -> int:
            if not node: return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.ans = max(self.ans, left + right + node.val)
            return max(left, right) + node.val

        # 错误提交
        # 1.没有考虑到节点中可能有负值，所以ans的初始化不能为0
        # 2.路径至少包含一个节点，也就是说可以不要左右子树中的一个，所以left 和right需要用max(i,0)包一下
        dfs(root)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
