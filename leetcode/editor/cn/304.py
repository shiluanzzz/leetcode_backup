# 304. {question.title}


# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:

    def __init__(self, matrix):
        self.pre_sum=[[0]*len(matrix[0]) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.pre_sum[row][col]=matrix[row][col]+self.get_pre_sum(row-1,col)+self.get_pre_sum(row,col-1)-self.get_pre_sum(row-1,col-1)
        # print(self.pre_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.get_pre_sum(row2,col2)-self.get_pre_sum(row1-1,col2)-self.get_pre_sum(row2,col1-1)+self.get_pre_sum(row1-1,col1-1)
        # print(ans)
        return ans
    def get_pre_sum(self,row,col):
        if row<0 or row>len(self.pre_sum):
            return 0
        if col<0 or col>len(self.pre_sum[0]):
            return 0

        return self.pre_sum[row][col]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a=NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    a.sumRegion(2,1,4,3)
    a.sumRegion(1,1,2,2)
    a.sumRegion(1,2,2,4)
