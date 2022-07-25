


def solve(candidates:list,target):
    # 分治法
    candidates.sort()
    res =[]

    def d(sum,ans,index):
        if sum==target:
            res.append(ans)
            return
        # ans:{n:[1,2,3,]}
        for d_index,each in enumerate(candidates[index:]):
            if sum+each==target:
                ans.append(each)
                res.append(ans.copy())
                return
            elif sum+each>target:
                return
            else:
                t=ans.copy()
                t.append(each)
                d(sum+each,t,index+d_index)
    for index,i in enumerate(candidates):
        d(i,[i],index)
    return res

solve([2,3,5],8)
solve([2,3,6,7],7)
solve([2,3,3,],2)
solve([2],499)
a=solve([2,7,6,3,5,1],9)
print(a)