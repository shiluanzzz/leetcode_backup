# 创建时间:2022-08-31 11:33:44
# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        gain.insert(0, 0)
        # return max(itertools.accumulate(gain))
        ans = 0
        for i, v in enumerate(gain[1:], 1):
            gain[i] += gain[i - 1]
            ans=max(ans,gain[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

    tools.test_func_batch(Solution().search, params)
