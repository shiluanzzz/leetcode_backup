

class Solution:
    def findEvenNumbers(self, digits):
        count=[0 for i in range(10)]
        for i in digits:
            count[i]+=1
        ans=[]
        def dfs(i,res):
            if i==4:
                ans.append(res)
                return
            else:
                for item,c in enumerate(count):
                    if c<=0:continue

                    if i==3 and item==0:
                        continue
                    if i==1 and item%2!=0:
                        continue
                    res+=item*pow(10,i-1)
                    count[item]-=1
                    dfs(i+1,res)
                    res-=item*pow(10,i-1)
                    count[item]+=1
        dfs(1,0)
        ans=sorted(ans)
        return ans

if __name__ == '__main__':
    print(Solution().findEvenNumbers([1,2,3,0]))