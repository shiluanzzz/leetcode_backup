# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


# 不能使用重复的数字
import time

# 先计数，在替代后插入，求解时在解码
def solve(candidates:list,target):
    # 分治法
    candidates.sort()
    res =[]

    def d(sum,ans,index):
        if sum==target:
            if ans not in res:
                res.append(ans)
            return

        for d_index,each in enumerate(candidates[index:]):
            if sum+each==target:
                ans.append(each)
                if ans not in res:
                    res.append(ans.copy())
                return
            elif sum+each>target:
                return
            else:
                t=ans.copy()
                t.append(each)
                if len(candidates)-(index+d_index+1)<(target-sum-each):
                    return
                else:
                    d(sum+each,t,index+d_index+1)

    for index,i in enumerate(candidates):
        d(i,[i],index+1)
    print(res)
    return res

solve([2,3,5],8)
solve([2,3,6,7],7)
solve([2,3,3,],2)
solve([2],499)
solve([2,7,6,3,5,1],9)
solve([10,1,2,7,6,1,5],8)
solve([2,5,1,2,2],5)
solve([3,3,],3)
solve([1,1,1,1],4)
t=time.time()
solve([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],28)
print(time.time()-t)