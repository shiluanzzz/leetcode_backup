# -*- coding:utf-8 -*-
# __author__ = "shitou6"

class Solution:
    def countAndSay(self, n: int):
        if n==1:return "1"

        def next_AndSay(ss:str):
            dd=[]
            q=ss[0]
            num=1
            for i in ss[1:]:
                if i==q:
                    num+=1
                else:
                    dd.append((q,num))
                    q=i
                    num=1
            dd.append((q,num))
            # print("dd:",str(dd))
            return dd
        i=1
        ans='11'
        while(i<n-1):
            i+=1
            ll=next_AndSay(ans)
            ans=""
            for ss,num in ll:
                ans+=str(num)+ss
            # print(ans)
        return ans
s=Solution()
s.countAndSay(5)