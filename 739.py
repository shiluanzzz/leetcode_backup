class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 维护一个递减的单调栈 存放下标
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while len(stack) and temperatures[i]>temperatures[stack[-1]]:
                index=stack.pop()
                ans[index]=i-index
            stack.append(i)
        return ans
print(Solution().dailyTemperatures( [73,74,75,71,69,72,76,73]))