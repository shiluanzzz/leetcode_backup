# 创建时间:2022-09-06 15:23:10


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        def solver(nums):
            if not nums: return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = solver(nums[0:mid])
            root.right = solver(nums[mid + 1:len(nums)])
            return root
        return solver(nums)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
    # tools.test_func_batch(Solution()., params)
