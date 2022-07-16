# 1995. 统计特殊四元组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        self.ans=0
        visited=[0]*len(nums)
        def dfs(n,before):
            if len(n)==4:
                if sum(n[:3])==n[3]:
                    print(n)
                    self.ans+=1
                return
            for i,v in enumerate(visited):
                if not v and i>before:
                    n.append(nums[i])
                    visited[i]=1
                    dfs(n,i)
                    n.pop()
                    visited[i]=0
                    # before=nums[i]
        dfs([],-1)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().countQuadruplets(
[1,2,3,4,2,2,4,5,6,7,8,9,11,12,12,14,15,16,7,2,3,4,5]))