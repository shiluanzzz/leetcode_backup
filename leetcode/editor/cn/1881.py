# 1881. 插入后的最大值


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]!='-':
            for i,v in enumerate(n):
                if v<x:
                    return n[:i]+str(x)+n[i:]
            return n+str(x)
        else:
            # 负值
            for i in range(len(n)-1,0,-1):
                if int(n[i])<x:
                    return n[:i+1]+str(x)+n[i+1:]
            return '-'+str(x)+n[1:]

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().maxValue("-42524",3))