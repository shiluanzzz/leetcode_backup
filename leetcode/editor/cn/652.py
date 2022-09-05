# 创建时间:2022-09-05 09:46:25

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visited = collections.defaultdict(int)
        self.ans = []

        def dfs(node):  # 前序遍历结果
            if not node: return "#"
            left = dfs(node.left)
            right = dfs(node.right)
            v = ("{},{},{}".format(node.val,left,right))
            print(v)
            # v = ",".join([left, str(node.val), right])
            if visited[v] == 1:
                self.ans.append(node)
            visited[v] += 1
            return v
        dfs(root)
        # [print(str(i)) for i in self.ans]
        # for k,v in visited.items():
        #     print(k,v)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
    # tools.test_func_batch(Solution()., params)
