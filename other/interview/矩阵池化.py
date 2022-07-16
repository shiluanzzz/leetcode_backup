# 留下矩阵中第二大的数字
# 网易2022秋招，通用技术-算法A卷 0918
import pprint
def solve(matrix):
    n = len(matrix)
    M = matrix
    i, j = 0, 0
    for step in range(2,n,2):
        for i in range(0, n, step):
            for k in range(0, n, step):
                d = [M[i][k], M[i][k + step-1], M[i + step-1][k], M[i + step-1][k + step-1]]
                d.sort()
                M[i][k], M[i][k + step-1], M[i + step-1][k], M[i + step-1][k + step-1]=d[-2],d[-2],d[-2],d[-2]
                # pprint.pprint(M)
                # a=input()
                # print("-"*20)
        pprint.pprint(M)
        print("-"*20)

if __name__ == '__main__':
    solve([
        [1, 2, 3, 4, 5, 6, 7, 8],
        [2, 3, 4, 1, 5, 6, 3, 2],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [2, 3, 4, 1, 5, 6, 3, 2],
        [2, 3, 4, 1, 5, 6, 3, 2],
        [2, 3, 4, 1, 5, 6, 3, 2],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [2, 3, 4, 1, 5, 6, 3, 2],
    ])
