import random


def quick_sort(arr, left, right):
    # print("in:", arr[left:right + 1])
    if left >= right:
        return arr
    pivot = arr[left]
    # j = 0
    low, high = left, right
    while low < high:
        # 右边拿一个比基准小的数与之交换
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]
        # 从左边开始拿一个比基准大的数与之交换
        while low < high and arr[low] <= pivot:
            low += 1
        arr[low], arr[high] = arr[high], arr[low]
    # low 就是最终pivot所在的位置
    quick_sort(arr, 0, low - 1)
    quick_sort(arr, low + 1, right)
    return arr


n = 10
arr = [random.randint(0, 10) for _ in range(n)]
print("原始数组", arr)
# arr = [0, 2, 6, 7, 8, 8, 3, 0, 5, 5]
print("快排结果", quick_sort(arr, 0, len(arr) - 1))
