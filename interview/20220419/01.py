from operator import ne


# inputA=[int(i) for i in input().split()]
# N,P=inputA[0],inputA[1]
# need=[int(i) for i in input().split()]
N,P=6,5
need=[100 ,1 ,3 ,0 ,10 ,100]
dp=[0]+[float('inf')]*(len(need)-1)
def dfs(i):
    if dp[i]!=float('inf'):
        return dp[i]
    dp[i]=min(
            max(0,need[i-1]-need[i]),
            P,
        )
    if i<N-1:
        dp[i]=min(
            dp[i],
            max(0,need[i+1]-need[i]),
        )
    return dp[i]

for i in range(N):
    dfs(i)
print(dp)
print(sum(dp))