from bisect import bisect_right


inputA=[int(i) for i in input().split()]
N,M=inputA[0],inputA[1]
task_times=[int(i) for i in input().split()]
for i in range(1,len(task_times)):
    task_times[i]+=task_times[i-1]
def solve(time):
    j=bisect_right(task_times,time)
    return j
for i in range(M):
    a=int(input())
    print(solve(a))