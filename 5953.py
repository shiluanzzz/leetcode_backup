import heapq


class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n=len(nums)
        self.ans=0
        for i in range(n):
            min_v,max_v=nums[i],nums[i]
            for k in range(i+1,n):
                min_v=min(nums[k],min_v)
                max_v=max(nums[k],max_v)
                self.ans += max_v - min_v

        return self.ans
if __name__ == '__main__':

    a=Solution().subArrayRanges([4,-2,-3,4,1])
    print(a)