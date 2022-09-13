# 创建时间:2022-09-09 14:52:28

## 十大排序算法
# leetcode submit region begin(Prohibit modification and deletion)
import random


class Solution:
    # 冒泡算法
    def sortArray(self, nums: list[int]) -> list[int]:
        pass

    def bubble_sort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    # 选择排序
    def select_sort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            v, idx = nums[0], 0
            for j in range(len(nums) - i):
                if nums[j] > v:
                    v, idx = nums[j], j
            # 交换
            nums[len(nums) - i - 1], nums[idx] = nums[idx], nums[len(nums) - i - 1]
        return nums

    def insert_sort(self, nums: list[int]) -> list[int]:
        # 前i个元素是有序的，把第i个元素插入到有序的数组中
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            while j > 0 and nums[j - 1] > temp:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = temp
        return nums

    # TODO
    def shell_sort(self, nums):
        # 划分间隔，对每个间隔里进行插入排序然后在细分间隔.
        gap = len(nums) // 2
        size = len(nums)
        while gap > 0:
            # i是每个间隔的起点
            for i in range(gap, size):
                temp = nums[i]
                j = i
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[i] = temp
            gap //= 2
        return nums

    def merge_sort(self, nums):
        # 把当前的序列划分成两个子序列，然后对子序列排序后合并两个有序的子序列
        def merge_arr(arr1, arr2):
            ans = []
            i, j = 0, 0
            # 合并两个有序的数组
            while i < len(arr1) or j < len(arr2):
                if i >= len(arr1):
                    ans.append(arr2[j])
                    j += 1
                    continue
                if j >= len(arr2):
                    ans.append(arr1[i])
                    i += 1
                    continue
                if arr1[i] < arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                else:
                    ans.append(arr2[j])
                    j += 1
            return ans

        def sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            return merge_arr(sort(nums[0:mid]), sort(nums[mid:]))

        return sort(nums)

    def count_sort(self, nums):
        min_v, max_v = min(nums), max(nums)
        cnt = [0] * (max_v - min_v + 1)
        for v in nums:
            cnt[v - min_v] += 1
        res = []
        for i, v in enumerate(cnt):
            res = res + [min_v + i] * v
        return res

    def quick_sort(self, nums):
        def _sort(nums, left, right):
            if left >= right:
                return
            low, high = left, right
            base = nums[low]
            while low < high:
                while low < high and nums[high] >= base:
                    high -= 1
                nums[high], nums[low] = nums[low], nums[high]
                while low < high and nums[low] <= base:
                    low += 1
                nums[high], nums[low] = nums[low], nums[high]
            _sort(nums, left, low - 1)
            _sort(nums, low + 1, right)
            return nums

        return _sort(nums, 0, len(nums) - 1)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    from leetcode import tools

    size = 10
    arr = [random.randint(0, 10) for _ in range(size)]

    # tools.test_func(Solution().bubble_sort, arr[:])
    # tools.test_func(Solution().select_sort, arr[:])
    # tools.test_func(Solution().insert_sort, arr[:])
    tools.test_func(Solution().shell_sort, arr[:])
    tools.test_func(Solution().merge_sort, arr[:])
    tools.test_func(Solution().count_sort, arr[:])
    tools.test_func(Solution().quick_sort, arr[:])
