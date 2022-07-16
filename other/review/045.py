class Solution:
    def jump(self, nums: list[int]) -> int:
        max_dist = nums[0]
        ans = 0
        begin = 0
        while max_dist < len(nums) - 1:
            print(begin, max_dist)
            b, t = begin, max_dist
            for i in range(begin + 1, max_dist + 1):
                if i + begin + nums[i] > t:
                    t, b = i + begin + nums[i], begin + i
            begin, max_dist = b, t
            ans += 1
        return ans + 1


if __name__ == '__main__':
    print(Solution().jump(
        [2, 3, 0, 1, 4, 0, 0, 1, 1, 3, 2, 1, 1, 3, 3, 1])
    )
