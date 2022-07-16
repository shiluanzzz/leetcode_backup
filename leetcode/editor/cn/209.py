# 209. 长度最小的子数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution2:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        self.ans = len(nums) + 1
        print("len",len(nums))
        hash={}
        def find_target(q, p):
            key="{}-{}".format(q,p)
            if key in hash:
                return
            else:
                hash[key]=1
            if p > len(nums) or q > p:
                return
            if sum(nums[q:p + 1]) >= target:
                self.ans = min(self.ans, p + 1 - q)
                find_target(q +1,p)
            find_target(q, p + 1)
        find_target(0, 0)
        if self.ans==len(nums)+1:
            return 0
        else:
            return self.ans

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if nums[0]>=target:return 1
        ans=len(nums)+1
        for i,v in enumerate(nums[1:],1):
            nums[i]=v+nums[i-1]
            if nums[i]>=target:ans=min(ans,i+1)
            left=i-ans if i-ans>=0 else 0
            while nums[i]-nums[left]>=target and left<i:
                ans=min(ans,i-left)
                left+=1
        if ans==len(nums)+1:return 0
        return ans

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().minSubArrayLen(
        7,[1,2,3,1]
    ))