# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
import time



def s(x,a,b,n):
    data={}
    def solve2(x,a,b,n):
        if n==0:
            return 0
        def do(x,a,b,n):
            data.setdefault(n,{})
            temp=data.get(n).get(x)
            if temp is not None:
                return temp
            else:
                temp=x+solve2(x-a if x>a else x,a,b,n-1)
                data[n][x]=temp
            return temp

        def notdo(x,a,b,n):
            data.setdefault(n,{})
            temp=data.get(n).get(x)
            if temp !=None:
                return temp
            else:
                temp=solve2(x+b,a,b,n-1)
                data[n][x]=temp
            return temp
        return max(do(x,a,b,n),notdo(x,a,b,n))
    return solve2(x,a,b,n)
if __name__ == '__main__':
    t=time.time()
    print(s(10,5,5,100))
    print(time.time()-t)