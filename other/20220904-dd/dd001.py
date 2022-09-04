import heapq


def solve2(nums, k):
    nums.sort()
    sum, ans = 0, 0
    for i in range(len(nums)):
        sum += nums[i]
        if (sum * k) >= nums[i] * (i + 1):
            ans = i + 1
        else:
            sum -= nums[i]
    return ans


def solve(nums: list, k: int):
    # k倍
    # nums.sort()
    now = [-i for i in nums]
    heapq.heapify(now)
    weight = sum(nums)
    count = len(nums)
    while now and (-now[0]) > (weight / count) * k:
        item = heapq.heappop(now)
        count -= 1
        weight += item
    return count


print(solve([3, 10, 5, 4, 2], 2))
