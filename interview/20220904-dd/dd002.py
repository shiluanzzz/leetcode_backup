import functools
import time

params = """
2
0 1
0 10
0 1
"""


@functools.cache
def cal(a, b):
    return a ^ b


@functools.cache
def OR(a: str):
    if len(a) == 1:
        return int(a)
    else:
        return cal(int(a[0]), OR(a[1:]))
        # return int(a[0])^OR(a[1:])
    # ans=0
    # n=[int(i) for i in a]
    # for i in n:
    #     ans ^= int(i)
    # return ans


be = time.time()
for i in range(0, 700001):
    OR(str(i))
print(time.time() - be)

input()
L = [int(i) for i in input().split(" ")]
R = [int(i) for i in input().split(" ")]
I = [int(i) for i in input().split(" ")]
ans = []


def solve(left, right, key):
    ans = 0
    for i in range(left, right + 1):
        if OR(i) == key:
            ans += 1
    return ans


for i in range(len(L)):
    ans.append(str(solve(L[i], R[i], I[i])))
print(" ".join(ans))
