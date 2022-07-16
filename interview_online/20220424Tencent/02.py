
class Solution:
    def getNumber(self , a ):
        def cut(arr):
            # 2 3 
            arr[0]=0
            ans=[]
            for i in range(len(arr)):
                if arr[i]!=0:
                    ans.append(arr[i])
                    bei=2
                    i+=1
                    while bei*i<len(arr):
                        arr[bei*i-1]=0
                        bei+=1
            return ans
        while len(a)>3:
            a=cut(a)
            # print(a)
        return a[1]
import random
test=[]
for i in range(10000):
    test.append(random.randint(0,10))
print(Solution().getNumber(test))
# print(Solution().getNumber([3,1,1,4,5,6,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2]))