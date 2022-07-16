# 1414. 和为 K 的最少斐波那契数字数目


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fb=[1,1]
        a,b=1,1
        while b<k:
            a,b=b,a+b
            fb.insert(0,b)
        print(fb)
        def dfs(num,count):
            for i in fb:
                if i>num:
                    continue
                if i==num:
                    print(i)
                    return count+1
                if i<num:
                    print(i)
                    return dfs(num-i,count+1)
        return dfs(k,0)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().findMinFibonacciNumbers(300912))