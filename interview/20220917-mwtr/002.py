import collections
import heapq
import random


def solve2(x, y, nums: list):
    counter = collections.Counter(nums)
    nums = list(set(nums))
    print(nums)
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            op1 = (nums[i] * nums[j] >= y)
            op2 = (nums[i] + nums[j] >= x)
            if op1 and op2:
                # print(nums[i], nums[j])
                if i != j:
                    b = counter[nums[i]] * counter[nums[j]]
                    # print("1111:", b)
                    ans += b
                else:
                    b = sum(range(counter[nums[i]] - 1, 0, -1))
                    ans += b
    print(ans)
    return (ans)


def solve(x, y, nums: list):
    nums.sort()
    ans = 0
    for i, v in enumerate(nums):
        j = len(nums) - 1
        op1 = (nums[i] * nums[j] >= y)
        op2 = (nums[i] + nums[j] >= x)
        if not op1 or not op2:
            continue
        for j in range(i + 1, len(nums)):
            op1 = (nums[i] * nums[j] >= y)
            op2 = (nums[i] + nums[j] >= x)
            if op1 and op2:
                ans += len(nums) - j
                break
    print(ans)
    return (ans)


x, y = 6, 8
arr = [random.randint(1, 10) for _ in range(10)]
# arr = [1, 2, 2, 3, 3, 4, 5, 6]
# arr.sort()
# print(arr)
assert solve(x, y, arr) == solve2(x, y, arr), print(arr)
