#
# @lc app=leetcode.cn id=825 lang=python3
#
# [825] 适龄的朋友
#

# @lc code=start
from collections import Counter
import collections
from dataclasses import dataclass
import itertools


class Solution:
    # 20220716 超时
    def numFriendRequests_1(self, ages: list[int]) -> int:
    #    只会往年龄比自己大的发送请求
    #    第三个限制条件
        ans=0
        for i,x in enumerate(ages):
            for j,y in enumerate(ages):
                if i==j:
                    continue
                if y>x or y<=0.5*x+7 or (y>100 and x<100):
                    continue
                ans+=1
        return ans
    # review
    def numFriendRequests(self, ages: list[int]) -> int:
        # 第二个条件是与第三个条件重合的，条件二满足的时候，条件3肯定也会满足，所以说两个条件重回了。
        # 对于第一个条件，就是求一个区间的人数，区间人数使用前缀和求解
        datas=[0]*(max(ages)+1)
        for i in ages:datas[i]+=1
        nums = list(itertools.accumulate(datas))
        ans = 0
        for age in set(ages):
            # 最后一个减1 是减去自己
            ans+= datas[age]*max(0,(nums[age]-nums[age//2+7]-1))
        return ans


    def numFriendRequests_3(self, ages: list[int]) -> int:
        data = [0] * (max(ages) + 1)
        for age in ages: data[age] += 1
        # pre_sum=[data[0]]+[0]*(len(data)-1)
        # for i in range(1,len(pre_sum)):
        #     pre_sum[i]=data[i]+pre_sum[i-1]
        # 前缀和的求解可以使用下面的这个内置函数
        pre_sum = list(itertools.accumulate(data))
        ans = 0
        for age in set(ages):
            ans += data[age] * max(0, pre_sum[age] - pre_sum[age // 2 + 7] - 1)
        return ans
# @lc code=end

