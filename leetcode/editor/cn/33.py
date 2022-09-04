# 33. 搜索旋转排序数组

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search2(self, nums: list[int], target: int) -> int:
        # 从有序的数组中找数第一时间想到二分
        # 解法：先找到旋转点，然后对前后的两个部分进行二分，时间复杂度O(n)，
        # 就是一开始找旋转点的时间复杂度
        def find(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        idx = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                idx = i
                break
        res = find(nums, 0, idx, target)
        if res != -1: return res
        res = find(nums, idx, len(nums) - 1, target)
        if res != -1: return res
        return -1

    def search(self, nums: list[int], target: int) -> int:
        # 先通过二分的思想，找到旋转点，然后对剩下的部分进行二分
        if len(nums) == 0: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        print("mid", (l + r) // 2)
        if target >= nums[0]:
            l = 0
        else:
            l = l + 1
            r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    [4,5,6,7,0,1,2]
    0
    [4,5,6,7,0,1,2]
    5
    [4,5,6,7,0,1,2]
    6
    [4,5,6,7,0,1,2]
    7
    [4,5,6,7,0,1,2]
    3
    [4,5,6,7,0,1,2]
    2
    """
    from leetcode import tools

    tools.test_func_batch(Solution().search, params)
