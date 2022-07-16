# 验证递归中的记忆存储优化性能
import time


def fib_1(n):
    if n==0: return 0
    if n==1: return 1
    return fib_1(n-1)+fib_1(n-2)

def fib_2(n):
    cache={
        0:0,1:1
    }

    def solve(n):
        key = cache.get(n)
        if key!=None:
            return key
        else:
            key=solve(n-1)+solve(n-2)
            cache[n]=key
            return key
    return solve(n)

if __name__ == '__main__':
    # t=time.time()
    # print(fib_1(30))
    # print(time.time()-t)
    t=time.time()
    print(fib_2(900))
    print(time.time()-t)