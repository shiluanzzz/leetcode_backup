from idna import valid_contextj
from pyrsistent import b


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        lineset=[set() for _ in range(n)]
        colset=[set() for _ in range(n)]
        splitset=[set() for _ in range(n)]
        ok=set()
        for i in range(n):
            for j in range(n): 
                if board[i][j]=='.':continue
                ok.add((i,j))
                lineset[i].add(board[i][j])
                colset[j].add(board[i][j])
                splitset[(i//3)*3+j//3].add(board[i][j]) 
        num=[str(i) for i in range(1,10)]
        print(splitset)
        def back(i,j):
            # print(i,j)
            if i==n:
                return True
            if j==n:
                return back(i+1,0)
            if (i,j) in ok:
                return back(i,j+1)
            for may in num:
                if may not in lineset[i] and may not in colset[j] and may not in splitset[(i//3)*3+j//3]:
                    lineset[i].add(may)
                    colset[j].add(may)
                    splitset[(i//3)*3+j//3].add(may)
                    board[i][j]=may
                    
                    if back(i,j+1):
                        return True

                    board[i][j]='.'
                    lineset[i].remove(may)
                    colset[j].remove(may)
                    splitset[(i//3)*3+j//3].remove(may)
            return False
        print(back(0,0))
        for i in board:
            print(i)
        return 
t=[["5","3","4",".",".",".",".","1","2"],[".","7","2","1","9","5","3","4","8"],["1","9","8",".","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
t= [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(Solution().solveSudoku(t))