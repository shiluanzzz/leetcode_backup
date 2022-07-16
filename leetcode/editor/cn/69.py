# 69. Sqrt(x)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:return x
        l, r = 0, x // 2
        m=0
        while l <= r:
            m = (r + l) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
            else:
                return m
        if m*m>x:return m-1
        else:return m
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().mySqrt(15))