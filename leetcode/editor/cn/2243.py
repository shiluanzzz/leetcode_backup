class Solution:
    def digitSum(self, s: str, k: int) -> str:

        
        def cal(s):
            print("cal",s)
            return str(sum([int(i) for i in s]))

        def add(s):
            if len(s)<=k:return s
            ans=""
            for i in range(0,len(s),k):
                ans += cal(s[i:i+k])
            return add(ans)
        return add(s)
print(Solution().digitSum(s = "1111122222312312341234123412421", k = 2))