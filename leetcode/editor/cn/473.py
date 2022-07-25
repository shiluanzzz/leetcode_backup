# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴
# 都要用到。 
# 
#  输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,2,2,2]
# 输出: true
# 
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,3,3,3,4]
# 输出: false
# 
# 解释: 不能用所有火柴拼成一个正方形。
#  
# 
#  注意: 
# 
#  
#  给定的火柴长度和在 0 到 10^9之间。 
#  火柴数组的长度不超过15。 
#  
#  Related Topics 位运算 数组 动态规划 回溯 状态压缩 👍 223 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        lens=sum(matchsticks)
        if lens%4!=0:return False
        # 让火柴棍从大到小去组合 避免无意义的小火柴组合。
        matchsticks.sort(reverse=True)
        self.nums=matchsticks
        self.target=lens//4
        self.used=[0 for i in range(len(self.nums))]
        return self.backtrack(0,0)


    def backtrack(self,index,now_lens):
        if index==4:
            return True
        if now_lens==self.target:
            return self.backtrack(index+1,0)

        for i in range(len(self.nums)):
            if self.used[i]:
                continue
            if self.nums[i]+now_lens>self.target:
                return False
            elif self.nums[i]+now_lens<=self.target:
                # 递归 先占用这个位置
                self.used[i]=1
                if self.backtrack(index,now_lens+self.nums[i]):
                    return True
                # 无效 释放位置
                self.used[i]=0
        return False
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    input=[13,11,1,8,6,7,8,8,6,7,8,9,8]
    input=[3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]
    a=Solution().makesquare(input)
    print(a)