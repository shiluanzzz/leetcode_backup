# 464.我能赢吗
# 创建时间: 2022-08-18 10:23:37

# leetcode submit region begin(Prohibit modification and deletion)
import collections
import functools


class Solution:
    def canIWin1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 最基本的递归
        def dfs(cur: int, target: int, nums: list):
            for i, v in enumerate(nums):
                if cur + v >= target:
                    return True
                new_num = nums[:]
                new_num.pop(i)
                if not (dfs(cur + v, target, new_num)):
                    return True
            return False

        return dfs(0, desiredTotal, [i for i in range(1, maxChoosableInteger + 1)])

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 最基本的递归
        # dp压缩
        # 记忆化递归只存了statue。实际上递归的因素有两个cur和status，但是status就包含了cur的信息 是一一对应的。所以只记录了status
        lru = collections.defaultdict(int)

        def dfs(cur: int, target: int, status: int):
            if lru[status] == 1: return True
            if lru[status] == 2: return False
            for v in range(1, maxChoosableInteger + 1):
                # 已经用过的数字不在用
                if (1 << v) & status: continue
                if cur + v >= target:
                    lru[status] = 1
                    return True
                if not dfs(cur + v, target, (1 << v) | status):
                    lru[status] = 1
                    return True
            lru[status] = 2
            return False

        # 下面是两种剪枝的情况
        if maxChoosableInteger >= desiredTotal:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False
        return dfs(0, desiredTotal, 0)


# leetcode submit region end(Prohibit modification and deletion)


# main
if __name__ == "__main__":
    # import sys
    #
    # sys.path.append("D:\\project\\PyProject\\leetcode_record\\")
    # import tools

    # tools.test_func(Solution().xxx)
    print(Solution().canIWin(5, 50))
