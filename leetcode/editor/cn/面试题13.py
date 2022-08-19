# 面试题13.机器人的运动范围
# 创建时间: 2022-08-17 10:32:35

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if n == 0: return 1

        def judge(i, j):
            return sum(map(int, list(str(i) + str(j)))) <= k

        visited = [[0 for _ in range(n)] for _ in range(m)]
        visited[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                if not judge(i, j): continue
                if j >= 0 and visited[i][j - 1]:
                    visited[i][j] = 1
                    continue
                if i >= 0 and visited[i - 1][j]:
                    visited[i][j] = 1
                    continue

        # for i in visited:
        #     print(i)
        return sum([sum(i) for i in visited])


# leetcode submit region end(Prohibit modification and deletion)


# main
if __name__ == "__main__":
    # import sys
    #
    # sys.path.append("D:\\project\\PyProject\\leetcode_record\\")
    # import tools
    #
    # tools.test_func(Solution().xxx)
    print(Solution().movingCount(38, 15, 9))
