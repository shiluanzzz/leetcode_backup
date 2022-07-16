
task=[0]*5
count=1
hash={}
def dfs(r,index):
    global hash
    if r==0:
        if str(task) not in hash:
            hash[str(task)]=1
        return 1
    if r<0 or index>4:
        return 0

    task[index]=0
    dfs(r,index+1)

    task[index]=1
    dfs(r-1,index+1)
    task[index]=0

    task[index]=2
    dfs(r-2,index+1)
    task[index]=0

    task[index]=3
    dfs(r-3,index+1)
    task[index]=0
dfs(3,0)
print(len(hash))
for each in hash.keys():
    print(each)