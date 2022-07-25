
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        size = len(heights) + 2  #因为要前后分别要加一个哨兵，所以数组的总长度需要加1
        heights = [0] + heights + [0]  #前后分别加一个哨兵，方便使用单调栈
        stack = [0]#设置单调栈
        ans = 0  #初始数，用来存储最大值矩阵面积
        for i in range(1 , size):  #遍历数组
            while heights[i] < heights[stack[-1]]:#如果遇见了第一个小于当前栈顶在数组中的值，则需要将栈顶所存储的数组的值的序号弹出栈
                  hights = heights[stack.pop()] #将栈顶所存储的数组的值的序号弹出栈，作为高度，这说明这个高度能够跨越的宽度已经到头
                  widths = i - stack[-1] - 1  #求出栈弹出的的序号在数组中的值作为的高度所走过的宽度，
                  #因为不包括前后两个，只包括中间的 因此需要-1
                  ans = max(ans , hights*widths)   #每个求出的面积都需要跟原来的比较，方便求出最大的面积
            stack.append(i)   #根本上述的如果遇见的值大于栈顶的存储的序号在数组中的值，那么就将这个序号压入栈，
            #继续寻找小于栈顶存储序号在数组中的值
        print("ans",ans)
        return ans


import itertools
def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    ans = float('inf')
    pre_sum = list(itertools.accumulate(nums))
    for i, v in enumerate(pre_sum):
        if nums[i] >= target: return 1
        if v >= target:
            ans = min(ans, i + 1)
            # 每次都从第一个位置往前找肯定会超时，找出一个可能最短位置开始判断。
            begin = i + 1 - ans
            for j in range(begin, i - 1):
                if pre_sum[i] - pre_sum[j] >= target:
                    ans = min(ans, i - j)
                else:
                    break
            # 从后往前，在做一个剪枝

    return ans if ans != float('inf') else 0


# Solution().largestRectangleArea([2,1,5,6,2,3])
Solution().largestRectangleArea([2,1,2])