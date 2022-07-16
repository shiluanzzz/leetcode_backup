import collections
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
hand=[]
for i,v in enumerate(price[:-1]):
    if m>=v and find(i,v):
        hand.append(v)
        m-=v
    else:
        if hand:
            # print(i,"mai",v)
            hand.pop()
            m+=v
    hash[v]-=1
for i in hand:
    m+=price[-1]-i
print(m)