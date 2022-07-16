# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


def solve(intervals:list):
    intervals.sort(key=lambda x:x[0])
    i=0
    while i <len(intervals)-1:
        j=i+1
        while intervals[j][0]<=intervals[i][1]:
            intervals[i][1]=max(intervals[j][1],intervals[i][1])
            intervals.pop(j)
        else:
            i+=1
    return intervals

print(solve([[1,3],[2,5],[3,5],[7,8]]))