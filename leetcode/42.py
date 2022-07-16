class Solution:
    def trap(self, height: list[int]) -> int:
        # 用一个单调递减的栈来维护可以接的雨水滴。
        stack=[height[0]]
        ans=1
        for i in range(1,len(height)):
            if len(stack):
                q=len(stack)-1
                if height[i]>=stack[0]:
                    # 可以全部兜底
                    for each in stack:
                        ans+=stack[0]-each
                    stack=[]
                elif height[i]>stack[q]:
                    # 可以部分填平
                    while q>-1 and height[i]>stack[q]:
                        ans+=height[i]-stack[q]
                        stack[q]=height[i]
                        q-=1
            stack.append(height[i])
        return ans
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))
