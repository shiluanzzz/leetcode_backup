import collections
from functools import lru_cache
IN=[int(i) for i in input().split()]
n,m=IN[0],IN[1]
price=[int(i) for i in input().split()]
# m块钱 n天
# 后面有比当前价格高就买入 没有就卖出且不买
hash=collections.Counter(price)
def find(i,key):
    for k,v in hash.items():
        if v<=0:continue
        if k>key:return True
    return False
hand=0

@lru_cache(None)
def dfs(day,hand,m):
    ans=0
    if day==n-1:
        return m+price[-1]*hand
    else:
        if m>=price[day] and find(-1,price[day]):
            hand+=1
            m-=price[day]
            ans=dfs(day+1,hand,m)
            hand-=1
            m+=price[day]
            ans=max(ans,dfs(day+1,hand,m))
        else:
            if hand>0 and price[day]>price[-1]:
                m+=price[day]
                hand-=1
                ans=dfs(day+1,hand,m)
    return ans

print(dfs(1,0,m))