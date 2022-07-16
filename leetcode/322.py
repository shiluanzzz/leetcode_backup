import collections


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # coins.sort(reverse=True)
        # if amount==0:return 0
        # if coins[-1]>amount:return -1
        dd=collections.defaultdict(int)
        def dp(need,count):
            if dd[need]:return dd[need]
            if need==0:return count
            if need<0:return -1
            ans=0
            for i in coins:
                if i>need:continue
                t=dp(need-i,count+1)
                if t!=-1:
                    ans=min(ans,t) if ans else t
            dd[need]=ans
            return ans
        return dp(amount,0)

if __name__ == '__main__':
    print(Solution().coinChange([186,419,83,408],6249))