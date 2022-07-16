# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
# error ans
def insert(intervals,newInterval):
    i=0
    old=intervals
    todo=newInterval
    if len(intervals)==0:
        return [todo]

    while i<len(old):
        if todo[0]>=old[i][0]: # 区间可插入
            if i+1<len(old) and  todo[0]<=old[i][1]:
                old[i][1]=max(old[i][1],todo[1])
                while i<len(old)-1 and old[i][1]>=old[i+1][0]:
                    old[i][1]=max(old[i][1],old[i+1][1])
                    old.pop(i+1)
                return old

            if i==len(old)-1 and todo[0]<=old[i][1]:
                old[i][1]=max(old[i][1],todo[1])
                return old
        if todo[1]<=old[i][1] and todo[1]>=old[i][0]:
            old[i][0]=min(old[i][0],todo[0])
            while i>0 and old[i][0]<=old[i-1][1]:
                old[i][0]=min(old[i][0],old[i-1][0])
                old.pop(i-1)
        if todo[0]<=old[i][0] and todo[1]>=old[i][1]:
            old[i]=todo
            return old
        i+=1
    if todo[0]>=old[-1][1]:
        old.extend([todo])
    if todo[1]<=old[0][0]:
        old.insert(0,todo)
    return old

def solve(intervals,newInterval):
    old=intervals
    todo=newInterval
    flag=(False,0,0)
    i,n=0,len(intervals)
    while i<len(intervals):
        item=intervals[i]
        if todo[0]>=item[0] and todo[1]<=item[1]:
            break
        if todo[0]<=item[0] and todo[1] >=item[1]:
            intervals[i]=todo
            break
        if todo[0]>=item[0] and todo[0]<=item[1]:
            intervals[i][1]=max(intervals[i][1],todo[1])
            break
        if todo[1]>=item[0] and todo[1]<=item[1]:
            intervals[i][0]=min(intervals[i][0],todo[0])
            break
        if todo[0]>item[1]and i+1<len(intervals) and todo[1]<intervals[i+1][0]:
            intervals.insert(i+1,todo)
            return intervals
        i+=1
    k=0
    while k<len(intervals)-1:
         if intervals[k][1]>=intervals[k+1][0]:
             intervals[k][1]=max(intervals[k+1][1],intervals[k][1])
             intervals.pop(k+1)
         elif intervals[k][1]>=intervals[k+1][1]:
             intervals.pop(k+1)
         else:
             k+=1

    if todo[0]>=intervals[-1][1]:
        intervals.extend([todo])
    if todo[1]<=intervals[0][0]:
        intervals.insert(0,todo)
    return intervals


def solve2(intervals,newInterval):
    if newInterval[0]>intervals[-1][1]:
        intervals.extend([newInterval])
        return intervals
    if newInterval[1]<intervals[0][0]:
        intervals.insert(0,newInterval)
        return intervals
    if len(intervals)==0:
        return [newInterval]
    res=[]
    i=0
    while i<len(intervals):
        if intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
            continue
        elif intervals[i][0]>newInterval[1]:
            res.append(newInterval)
            res.extend(intervals[i:])
            return res
        else:
            q=min(intervals[i][0],newInterval[0])
            i+=1
            while i<len(intervals) and intervals[i][0]<=newInterval[1]:
                i+=1

            p=max(intervals[i-1][1],newInterval[1])
            res.append([q,p])
            res.extend(intervals[i:])
            return res

    return intervals

print(solve2([[1,5]],[0,6]))
print(solve2([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(solve2([[0,3],[6,9]],[4,7]))
print(solve2([[1,5]],[6,8]))
print(solve2([[5,6]],[0,1]))
print(solve2([[3,5],[12,15]],[6,6]))
print(solve2([[1,3],[6,8]],[4,7]))
print(solve2([[1,5],[6,8]],[0,9]))
print(solve2([[1,5]],[5,7]))
print(solve2([[1,5],[7,9]],[6,7]))
print(solve2([[1,5],[6,7]],[6,6]))
print(solve2([[1,2],[3,5],[6,7],[8,10],[12,16]],
             [4,8]))