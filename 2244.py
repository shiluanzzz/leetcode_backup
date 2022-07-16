import collections
from operator import ne
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        count=list(collections.Counter(tasks).values())
        print(count)
        ans=0
        for i in range(len(count)):
            if count[i]<2:
                return -1
            if count[i]%3==0:
                pass
            elif count[i]%3==1:
                ans+=1
                count[i]-=4
            else:
                ans+=1
                count[i]-=2
            ans+=count[i]//3
        return ans
print(Solution().minimumRounds([1,1,1,2,2,2,3,3]))