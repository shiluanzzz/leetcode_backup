# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 统计三元组的个数

# 0 <= i < j < k < arr.length


class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        ans=0
        lens=len(arr)
        for i in range(lens-2):
            for j in range(i+1,lens-1):
                if abs(arr[i]-arr[j]) > a:
                    continue
                for k in range(j+1,lens):
                    if abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        ans+=1
                        # print(i,j,k,":",arr[i],arr[j],arr[k])
        return ans
Solution().countGoodTriplets([3,0,1,1,9,7],7,2,3)
