class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort(reverse=True)
        def find(remain,begin,total):
            if remain==0:return total
            # for i,v in enumerate(used):
            for i in range(begin,len(coins)):
                # 无法组成剩下的 行不通
                if coins[i]>remain: continue
                # 用
                count=remain // coins[i]
                new_remain=remain%coins[i]
                planA=find(new_remain,i+1,total+count)
                if planA==-1:
                    return find(remain,begin+1,total)
                else:
                    return planA
            return -1
        return find(amount,0,0)

if __name__ == '__main__':
    print(Solution().coinChange([186,419,83,408],6249))