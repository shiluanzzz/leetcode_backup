n=int(input())
strlist=[]
ans=[]
import heapq
for i in range(n):
    strlist.append(input())
for i in range(len(strlist[0])):
    num=""
    for j in range(n):
        num+=strlist[j][i]
    heapq.heappush(ans,int(num))
while ans:
    print(heapq.heappop(ans),end=" ")
print()