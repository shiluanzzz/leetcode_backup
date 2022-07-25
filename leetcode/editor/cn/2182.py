#
# @lc app=leetcode.cn id=2182 lang=python3
#
# [2182] 构造限制重复的字符串
#

# @lc code=start
import collections
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = collections.Counter(s)
        h = []
        for i in counter.keys():
            heapq.heappush(h,[-ord(i),counter[i]])
        ans = ""
        while h:
            item =  heapq.heappop(h)
            if item[1]<=repeatLimit:
                # 如果没达到限制的长度，就直接加进去
                ans+=item[1]*(chr(-item[0]))
            else:
                # 达到了限制的长度
                ans+=repeatLimit*(chr(-item[0]))
                item[1]-=repeatLimit
                # 在拿一个出来
                if h:
                    item2 = heapq.heappop(h)
                    ans += chr(-item2[0])
                    item2[1]-=1
                    heapq.heappush(h,item)
                    if item2[1]:
                        heapq.heappush(h.item2)
        return ans 
    def repeatLimitedString2(self, s: str, repeatLimit: int) -> str:
        # repeatLimit-=1
        sList = list(s)
        sList.sort(key=lambda x:ord(x),reverse=True)
        eqNum=1
        notUsed={}
        for i in range(1,len(sList)):
            if sList[i]==sList[i-1]:
                eqNum+=1
            else:
                eqNum=1
            if eqNum>repeatLimit:
                # 尝试从后往前找 找不到的话就往前找一个
                do=False
                for j in range(i,len(sList)):
                    if sList[i]!=sList[j]:
                        sList[i],sList[j]=sList[j],sList[i]
                        do=True
                        break
                if not do:
                    for j in range(i,-1,-1):
                        if sList[i]!=sList[j] and sList[j+1]!=sList[i] and j not in notUsed :
                            notUsed[j]=True
                            sList[i],sList[j]=sList[j],sList[i]
                            do=True
                            break
                eqNum=1
        return "".join(sList)
# @lc code=end


a=Solution().repeatLimitedString("daisfghjasgfjgasjgfkaskdfahsgdhj",4)
print(a)