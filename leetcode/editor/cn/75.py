# 创建时间:2022-09-08 15:45:31

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # 基于快排做，以1为中轴
        def sort(nums, left, right):
            if left >= right: return nums

            low, high = left, right
            base = nums[low]
            while low < high:
                while low < high and nums[high] >= base:
                    high -= 1
                nums[low], nums[high] = nums[high], nums[low]
                while low < high and nums[low] <= base:
                    low += 1
                nums[low], nums[high] = nums[high], nums[low]
            # 下一次快排的位置，应该是left和right相关的
            sort(nums, left, low)
            sort(nums, low + 1, right)

        sort(nums, 0, len(nums) - 1)
        return nums

    def sortColors1(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 基于单指针的方法就是用一个指针指向0的位置，如果遇到元素是0就跟指针交换 指针加一
        # 然后在来一趟，对1做同样的操作只不过开始的位置是从0的指针位置开始
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        # 基于双指针 唯一需要考虑的是交换0的时候可能会把1交换到后面来，所以判断是否需要把这个1在交换回去
        p0, p1 = 0, 0
        # for i, v in enumerate(nums):
        i = 0
        while i < len(nums):
            v = nums[i]
            if v == 0:
                swap(i, p0)
                if p0 < p1:
                    swap(i, p1)
                p0, p1 = p0 + 1, p1 + 1
            elif v == 1:
                swap(i, p1)
                p1 += 1
            i += 1
        return nums


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    [2,0,2,1,1,0]
    [0,0,0,0,1,1,1,0,2]
    [2,2,1,2,1,1,1,0,0,2,1,0,2,1,2,2,1,1,1,1,1,0,2,0,2,0,2,2,1,0,2,1,0,2,1,2,0,0,0,0,2,1,1,2,0,1,2,2,0,0,2,2,0,1,0,1,0,0,1,1,1,0,0,2,2,2,1,0,0,2,1,0,1,0,2,2,1,2,1,1,2,1,1,0,0,2,1,0,0]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().sortColors, params)
