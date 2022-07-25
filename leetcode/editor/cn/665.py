class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        # 三个一对的比较
        if len(nums)<3:
            t=nums.copy().sort()
            return nums==t
        def check(i): # 检查[i-2:i]
            print(i)
            a,b,c=nums[i-2],nums[i-1],nums[i]
            if a<=b and b<=c:return 0
            if c<b and b<a:return 2
            if b>a and b>c:
                nums[i-1]=nums[i-2]
                return 1
            if c<b:
                nums[i]=nums[i-1]
                return 1
            if b<a and b<c:
                nums[i-1]=nums[i-2]
                print("b min")
                return 1
        count=0
        for i in range(2,len(nums)):
            count+=check(i)
            if count>1:return False
        return count<=1
print(Solution().checkPossibility([-1,4,2,3]))