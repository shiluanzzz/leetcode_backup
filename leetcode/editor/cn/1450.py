# 1450. 在既定时间做作业的学生人数

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans=0
        for i,v in enumerate(startTime):
            if v<=queryTime and endTime[i]>=queryTime:
                ans+=1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

    tools.test_func_batch(Solution()., params)
