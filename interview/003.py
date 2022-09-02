import collections

input = [2, 1, 4, 3, 6, 5, 0, 7]


def do(num, k):
    count, cur = 0, num[0]
    for i in range(1, len(num)):
        if cur > num[i]:
            count += 1
        else:
            count, cur = 0, num[i]
        if count >= k: return cur
    return cur


print(do([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 100000))

s = "A B 3|B A 1|B C 4|A C 5|C B 9"


def s3(s):
    dd = collections.defaultdict(int)  # dd为一个字典 存放点X到其他点的距离
    for line in s.split("|"):
        f, t, v = line.split(" ")
        dd[f] += int(v)
    ans, val = "", float('inf')
    for k, v in dd.items():
        if v < val:
            ans, val = k, v
    return ans


print(s3(s))
