# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 网格

def solve(n,m,data,w_data):


    def go(x,y,n,m,w):
        t=data.get((x,y))
        if t != None:
            for each in t:

                if each == (n,m):
                    return w+w_data.get((x,y,each[0],each[1]))
                else:
                    return
        return 0

if __name__ == '__main__':
    data={}
    w_data={}
    n,m,k=map(int,input().strip().split())
    for i in range(k):
        x,y,u,v,w =map(int,input().strip().split())
        w_data[(x,y,u,v)]=w
        data.setdefault((x,y),[])
        data[(x,y)].append([u,v])
    print(data)
    print(w_data)
    print(solve(n,m,data))