class Solution:
    def countDistinct(self, nums: list[int], hold: int, p: int) -> int:
        origin=nums.copy()
        nums[0]=1 if nums[0]%p==0 else 0
        for i in range(1,len(nums)):
            if nums[i]%p==0:
                nums[i]=1
            else:
                nums[i]=0
            nums[i]+=nums[i-1]
        ans=0
        print(nums)
        hash=dict()
        for lens in range(0,len(nums)):
            for end in range(lens,len(nums)):
                total=nums[end]-nums[end-lens]
                if total<=hold:
                    t=origin[end-lens:end+1]
                    if str(t) not in hash:
                        print(t)
                        ans+=1
                        hash[str(t)]=1
        if nums[-1]<=hold:
            ans+=1
        return ans
        
            
            
print(Solution().countDistinct(
    #1 2 3 4 5  6  7 8 9 10
    [5,11,17,13,16,9,4,9,20],
    7,
    1
))