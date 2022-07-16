import collections


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(3):
            dp[i]=i
        for i in range(3,n+1):
            for k in range(2,i):
                # 可以不继续往下剪，也可以继续往下剪，往下剪就是取dp里的值。
                dp[i]=max(dp[i],k*(i-k),k*dp[i-k])
        print(dp)
        return dp[n]

class Solution2:
    def cuttingRope(self, n: int) -> int:
        res=1
        # 2,3都没得选 只能是剪1 4=2*2
        while n>4:
            # 大于4的时候应当拆分出尽可能多的3
            res*=3
            n-=3
        res*=n
        res=res%int(1e9+7)
        return res
if __name__ == '__main__':
    print(Solution2().cuttingRope(1000))
