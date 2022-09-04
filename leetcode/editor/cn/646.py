# 创建时间:2022-09-03 10:34:29

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 为什么是对结尾的字符进行排序?
        # 因为到后面的时候默认前面都是已经符合条件的，
        pairs.sort(key=lambda x: x[1])
        prev = pairs[0][1]
        ans = 1
        for be, end in pairs[1:]:
            if be > prev:
                prev, ans = end, ans + 1
        return ans

    def findLongestChain2(self, pairs: List[List[int]]) -> int:

        # dp[i] 表示以pairs结尾的数对链 的最长
        # 计算dp[i]的时候，就需要在0 - (i-1)中找一个最长的符合要求的dp
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
    # tools.test_func_batch(Solution()., params)
