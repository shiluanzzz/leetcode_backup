import collections
import random

# ss = "ababaadsfasdfasdfasdfasdfasdfasdfasdf"
#
ss = "".join([chr(ord('a') + (random.randint(0, 26))) for _ in range(1000)])


# ss = input()

def idx(char):
    return ord(char) - ord('a')


target = set([1 << i for i in range(26)])

ans = 0
cache = collections.defaultdict(int)
for each in ss:
    new_cache = collections.defaultdict(int)
    for v, k in cache.items():
        v = v ^ (1 << idx(each))
        if v in target:
            ans += k
        new_cache[v] = k
    new_cache[1 << idx(each)] += 1
    cache.clear()
    cache = new_cache

    ans += 1
print(ans)
# def judge(list):
#     count = 0
#     for i in list:
#         if i % 2 == 1:
#             count += 1
#         if count > 1:
#             return False
#     if count == 1:
#         return True
#     else:
#         return False
#
#
# ans = len(ss)
# for i, v in enumerate(ss):
#     count = {idx(v)}  # 总数为奇数的下标
#     for j in range(i + 1, len(ss)):
#         new_idx = idx(ss[j])
#         if new_idx in count:
#             count.remove(new_idx)
#         else:
#             count.add(new_idx)
#         if len(count) == 1:
#             ans += 1
#         # print(count)
# print(ans)
