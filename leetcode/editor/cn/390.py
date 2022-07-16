# 390. 消除游戏


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastRemaining(self, n: int) -> int:
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2)) if n > 1 else 1

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    for i in range(1,10000000000):
        print(i,":",Solution().lastRemaining(i))