# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
# n m
# w1 w2 w3
# q1
# q2
# q3


def solve(nums,q):
    # nums.sort()
    for each in nums.keys():
        if nums.get(q+each):

            return each,q+each
    return -1,-1

if __name__ == '__main__':

    l = map(int,input().strip().split())
    l = map(int,input().strip().split())
    # 变
    nums = {i:i for i in l}

    q = []
    while True:
        try:
            l = map(int,input())
            q.append([i for i in l][0])
        except EOFError:
            break

    for each in q:
        ans = solve(nums,each)
        print(ans[0],ans[1])

    # n,m = input().split()
    # n,m = int(n),int(m)
    # nums = input()
    # q = []
    # for i in range(m):
    #     q.append(int(input()))
    # nums = nums.split(' ')
    # nums = [int(i) for i in nums]
    # for each in q:
    #     ans = solve(nums,each)
    #     print(ans[0],ans[1])


