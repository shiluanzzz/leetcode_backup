n = int(input())
nums = [int(i) for i in input().split(" ")]
nums.sort()
ans = float('inf')


def win(left):
    windows = list(range(left, left + n))
    temp = 0
    for i in range(n):
        temp += abs(windows[i] - nums[i])
    return temp


for val in range(min(nums), max(nums)):
    ans = min(ans,win(val))

print(ans)