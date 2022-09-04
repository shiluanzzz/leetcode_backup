# 创建时间:2022-09-02 12:32:03


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum2(self, root: TreeNode, sum: int) -> int:
        self.ans = 0

        # 常规的递归太深 报错了
        def dfs(node, target):
            if not node:
                return
            target -= node.val
            if target < 0: return
            if target == 0:
                self.ans += 1
            else:
                dfs(node.left, target)
                dfs(node.right, target)
            if node.val <= sum:
                dfs(node, sum)
            return

        dfs(root, sum)
        return self.ans

    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 面向解析做的: 把问题拆分成两个主问题和子问题
        # 主问题:当前节点的路径和有几个等于sum
        # 子问题：当前节点的子节点的主问题.
        def nodeSum(node, sum) -> int:

            if not node: return 0
            ans = 0
            sum -= node.val
            if sum == 0: ans += 1
            ans += nodeSum(node.left, sum)
            ans += nodeSum(node.right, sum)
            return ans

        def pathSum(node, sum) -> int:
            if not node: return 0
            ans = 0
            ans += nodeSum(node, sum)
            ans += pathSum(node.left, sum)
            ans += pathSum(node.right, sum)
            return ans

        return pathSum(root, sum)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

