# 创建时间:2022-09-02 12:17:11


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    #     # 如何处理 三个方向值都一样的情况？
    #     def dfs(node: TreeNode, target: int, val: int) -> int:
    #         child_len = 0
    #         if node.left and node.left.val == target:
    #             child_len = max(child_len, dfs(node.left, target, val + 1))
    #         if node.right  and node.right.val == target:
    #             child_len = max(child_len, dfs(node.right, target, val + 1))
    #         return val + child_len

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.ans = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0
            # 对于非自顶向下的dfs需要用一个全局变量记录我们需要的答案。
            self.ans = max(self.ans, left + right)
            return max(left, right)
        dfs(root)
        return self.ans
    def longestUnivaluePath1(self, root: Optional[TreeNode]) -> int:
        # 这个是自己写的,上面是参考的别人的答案,但是我的超时了
        if not root: return 0

        queue = collections.deque([root])
        self.ans = 0

        def val_path(node: TreeNode, val: int) -> int:
            # val_path 求的是左右子树中 符合条件的最长的边
            if not node: return 0
            if node.val != val:
                # 有可能是其他的长路径节点
                # val_path(node, node.val)
                queue.append(node)
                return 0
            left = val_path(node.left, val)
            right = val_path(node.right, val)
            # ans 只能用全局变量记录
            self.ans = max(self.ans, left + right)
            return 1 + max(val_path(node.left, val), val_path(node.right, val))

        while queue:
            root = queue.pop()
            val_path(root, root.val)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
