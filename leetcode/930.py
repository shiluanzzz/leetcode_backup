# -*- coding:utf-8 -*-
# __author__ = "shitou6"

# 滑动窗口 好像不太行
#   找那个 1 ,0,1 或者 1 0 0 1这样的 在计算前面的0个数
def numSubarraysWithSum(A: list, S: int) -> int:
    sum=0
    a,b=0,0
    while(b<len(A)):
        if A[a:b].count(1)==S:
            print("a:{},b:{}".format(a,b))
            sum+=1
            # 计算前面有0的情况。
            c=a
            while(c+1<b):
                if A[c]==0:
                    sum+=1
                    c+=1
                else:
                    break
        else:
            a+=1
            b+=1
    return sum

print(numSubarraysWithSum([1,0,1,0,1],2))