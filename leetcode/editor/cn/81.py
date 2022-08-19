# 81. 搜索旋转排序数组 II

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # 先找到2分点 然后在2分查找?
        # @TODO
# leetcode submit region end(Prohibit modification and deletion)



if __name__ == '__main__':
    params = """
    [[6,7,9]]
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    [[1,2,3],[4,5,6],[7,8,9]]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().spiralOrder, params)
