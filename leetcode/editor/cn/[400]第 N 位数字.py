# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  Related Topics 数学 二分查找 👍 209 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1-9 9
        10-99 90*2
        100-999 900*3
        1000-9999 9000*4
        """
        if n<104:return n
        minnum,maxnum=1,9
        pre,total=8,8
        c=1 #几位数
        # 找到区间
        while total<n:
            minnum,maxnum=minnum*10,maxnum*10+9
            c+=1
            pre,total=total,total+(maxnum-minnum+1)*c
        total=pre
        k,p=divmod(n-total,c)
        return str(minnum+k-1)[p]

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    for i in range(1000):
        print(Solution().findNthDigit(i))