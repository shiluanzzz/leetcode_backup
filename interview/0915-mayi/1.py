import math

a = 123
char = [chr(ord('a') + i) for i in range(26)]
# count = [int(math.pow(2, i)) for i in range(10)]
count = {
    i: int(math.pow(2, i)) for i in range(10) for i in range(10)
}
# print(count)


def dfs(num, ans: list):
    if num <= 0:
        return False
    if num == 1:
        ans.append(0)
        return ans
    for i in range(9, -1, -1):
        if count[i] == num:
            ans.append(i)
            return ans
        if count[i] > num:
            continue
        t = dfs(num - count[i], ans[:])
        if t:
            # print(num - count[i], t)
            t.append(i)
            return t
    return False


ll=dfs(123, [])
ans=""
for v in ll:
    ans+=char[v]
print(ans)
