from functools import lru_cache


n=int(input())
nums=[]
for _ in range(n):
    nums.append([int(i) for i in input().split()])

# @lru_cache(None)
# def dfs(i,j):
#     if i==n-1:
#         return nums[i][j]
#     return nums[i][j]+max(dfs(i+1,j),dfs(i+1,j+1))
# dfs.cache_clear()
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        nums[i][j]+=max(nums[i+1][j],nums[i+1][j+1])
    
if n<=0:
    print(0)
else:
    print(nums[0][0])
