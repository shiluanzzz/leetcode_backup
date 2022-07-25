import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        h = []
        for i in range(0, len(arr)):
            for k in range(i, len(arr)):
                num = [arr[i] / arr[k], arr[i], arr[k]]
                heapq.heappush(h,num)
        ans=heapq.heappop(h)
        return [ans[1],ans[2]]

if __name__ == '__main__':
    Solution().kthSmallestPrimeFraction([1,29,47],1)