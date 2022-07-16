# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
import heapq
import random


def solve(str,op:list):

    dui=[]
    for each in op:
        heapq.heappush(dui,each)

    i=0
    a=[]
    while i<len(dui):
        q=heapq.heappop(dui)
        p=heapq.heappop(dui)
        if q==p:
            continue
        if q[0]>=p[0] and q[1]<p[1]:
            heapq.heappush(dui,[p[0],q[0]])
            heapq.heappush(dui,[p[1],q[1]])
        else:
            a.extend([q,p])
            i+=1
    print(a)
    print(dui)


if __name__ == '__main__':
    n=10
    l=[]
    for i in range(n):
        l.append(sorted([random.randint(0,10),random.randint(0,10)]))

    print(l)

    solve("1",l)