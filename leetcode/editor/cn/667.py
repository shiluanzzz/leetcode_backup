# 创建时间:2022-09-08 15:06:22

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # k=1 [1 2 3 ... n]
        # k=n-1 [1,n,2,n-1,3,n-2...]
        # 构造k-1个不同的差，然后剩下的按照升序排列去构造全部是1的排列
        # 如何构造不同的差? 就是[1,n,2,n-1...]这样
        ans = []
        for i in range(1, (k + 1) // 2 + 1):
            ans.append(i)
            ans.append(k + 2 - i)
        if k % 2 == 0:
            ans.append(1 + k // 2)
        return ans + [i for i in range(k + 2, n + 1)]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools
    # tools.test_func_batch(Solution()., params)
