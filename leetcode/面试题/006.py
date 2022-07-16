
def solve6(s,numsRows):
    ans=[]
    for i in range(numsRows):
        ans.append([])
    # n=3 0,1,2,1, ...
    # n=4 0,1,2,3,2,1 ...
    base=[i for i in range(numsRows)]+[i for i in range(numsRows-2,0,-1)]
    for index,item in enumerate(s):
        row=base[index%len(base)]
        ans[row].append(item)

    s=""
    for i in ans:
        for k in i:
            s+=k
    return s

if __name__ == '__main__':
    solve6("123456",2)