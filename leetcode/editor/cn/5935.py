class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        if time==0:
            return [i for i in range(len(security))]
        time+=1
        n=len(security)
        decend=[0]*n
        acend=[0]*n

        def judge(nums,reverse=True):
            # print(nums,reverse)
            for i in range(1,len(nums)):
                if nums[i-1]==nums[i]:
                    continue
                if (nums[i-1]<=nums[i]) != reverse:
                   continue
                else:
                    return False
            return True
        for i in range(n):
            if i-time+1 >= 0 and judge(security[i-time+1:i+1]):
                decend[i]=1
            if i+time <= n and judge(security[i:i+time],False):
                acend[i]=1
        print(decend)
        print(acend)
        ans=[]
        for i in range(n):
            if acend[i] and decend[i]:
                ans.append(i)
        return ans

if __name__ == '__main__':
    a=Solution().goodDaysToRobBank([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8],2)
    print(a)