class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        a=nums.copy()
        a.sort(reverse=True)
        a=a[:k]
        ans=[]
        for v in nums:
            if v in a:
                ans.append(v)
                a.remove(v)
        return ans

if __name__ == '__main__':
    a=Solution().maxSubsequence([-1,-2,-3,4,5,6],5)
    print(a)