import itertools


class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        data=[0]*(max(ages)+1)
        for age in ages:data[age]+=1
        # pre_sum=[data[0]]+[0]*(len(data)-1)
        # for i in range(1,len(pre_sum)):
        #     pre_sum[i]=data[i]+pre_sum[i-1]
        # 前缀和的求解可以使用下面的这个内置函数
        pre_sum=list(itertools.accumulate(data))
        ans=0
        for age in set(ages):
            ans+= data[age]*max(0,pre_sum[age]-pre_sum[age//2+7]-1)
        return ans

if __name__ == '__main__':
    print(Solution().numFriendRequests([16,17,18]))