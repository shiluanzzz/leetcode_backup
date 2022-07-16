class Solution:
    def movingCount(self, m: int, n: int, kk: int) -> int:

        def cal(num):
            return sum([int(i) for i in str(num)])

        ans = 0
        for i in range(m):
            sum_i = cal(i)
            max_k = n
            for k in range(n):
                if cal(k) + sum_i > kk:
                    ans += (i + 1) * (k)
                    max_k=k-1
            ans+=max_k

        return ans
if __name__ == '__main__':
    print(Solution().movingCount(3,2,17))       
