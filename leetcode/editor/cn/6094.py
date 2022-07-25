class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        s,n=set(),len(nums)
        for i in range(n):
            cnt=0
            for j in range(i,n):
                if nums[j]%p==0:
                    cnt+=1
                    if cnt>k:
                        break
                s.add(tuple(nums[i:j+1]))
        return len(s)

