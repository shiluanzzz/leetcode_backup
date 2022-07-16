import collections
# from curses.ascii import SO
from itertools import count
class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        counter=collections.Counter(arr)
        target=len(arr)
        if counter.get(0) and counter.get(0)%2==0:
            target-=counter.get(0)
            counter[0]=0

        def back(i):
            if i==target:return True
            for k,v in counter.items(): 
                if v==0:continue
                if k%2==0 and counter.get(k//2):
                    # 每次只减去最小的数
                    continue
                if counter.get(k*2):
                    if counter.get(k*2)<v:
                        return False
                    print("{},{} sub {}".format(k,k*2,v))
                    counter[k]-=v
                    counter[k*2]-=v
                    return back(i+2*v)
                else:
                    return False
        return back(0)
a=[33,-11,72,40,-3,78,-6,36,-12,32,64,-22,7,66,-92,14,-50,80,23,-100,35,-25,40,-40,-46,18,-15,-20,-24,-70,40,-12,82,-34,41,36,-98,-50,96,-30,-35,-49,-24,35,-68,-24,48,-6,46,-12,39,-22,-12,70,80,36,80,70,-22,18]
print(Solution().canReorderDoubled(a))
print(Solution().canReorderDoubled([2,4,0,0,1,8]))