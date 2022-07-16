N=int(input())
ans=0
for i in range(N):
    ans+= sum([int(i) for i in input().split()])
print(ans)