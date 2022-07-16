# 303. {question.title}


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    def __init__(self, nums: List[int]):
        self.array=[0]*len(nums)
        self.array[0]=nums[0]
        for i,v in enumerate(nums[1:],1):
            self.array[i]=self.array[i-1]+v
        print(self.array)

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.array[right]
        else:
            return self.array[right]-self.array[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
