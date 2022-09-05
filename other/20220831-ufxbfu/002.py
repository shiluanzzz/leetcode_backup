#
class Solution:
    def nucleicAcidTestWay(self, n: int) -> int:
        # write code here
        # 第i天做 第i+1,i+2天都不用做
        self.ans = 0

        def dfs(prev, now, do):  # 上一次做事什么时候
            if now > n: return
            if now - prev > 2: return
            if n - prev <= 2 and now == n:
                print(prev, now, do)
                self.ans += 1
            dfs(prev, now + 1, do + [0])
            dfs(now, now + 1, do + [1])
            return

        dfs(0, 1, [0])
        return self.ans


print(Solution().nucleicAcidTestWay(5))
