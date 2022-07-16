# 剑指 Offer 56 - II. 数组中数字出现的次数 II


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        t=0
        for num in nums:
            t^=num
            print(t,":",bin(t))
        print(t)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().singleNumber([3,4,3,3]))