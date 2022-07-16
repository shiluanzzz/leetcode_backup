# 794. {question.title}


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        # 字符数
        count_x,count_o=0,0
        for i in board:
            for v in i:
                if v=='X':
                    count_x+=1
                elif v=='O':
                    count_o+=1
                else:pass
        if count_o!=count_x and count_o!=count_x-1:
            return False
        if self.judge('X',board) and self.judge('O',board):return False
        if self.judge('X',board):
            if count_x!=count_o+1:return False
            return True
        if self.judge('O',board):
            if count_o!=count_x:return False
            return True
        return True
    def judge(self,c,board):
        def equal(c1,c2,c3,c4):
            if c1==c2 and c2==c3 and c3==c4:
                return True
            return False

        for each in board:
            if each==c*3:
                return True

        for i in range(3):
            if equal(c,board[0][i],board[1][i],board[2][i]):
                return True

        return equal(c,board[0][0],board[1][1],board[2][2]) or equal(c,board[0][2],board[1][1],board[2][0])
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().validTicTacToe(["XXX","OOX","OOX"]))