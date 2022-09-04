#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#

# @lc code=start
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    # 看似很可怕的题目，主要在与划分矩阵
    def construct(self, grid: list[list[int]]) -> 'Node':
        if self.is_leaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        else:
            a, b, c, d = self.split_matrix(grid)
            return Node(1, False,
                        self.construct(a),
                        self.construct(b),
                        self.construct(c),
                        self.construct(d)
                        )
    def is_leaf(self, grid):
        s = sum(sum(i) for i in grid)
        if s == 0 or s == len(grid) * len(grid):
            return True
        return False

    def split_matrix(self, grid):
        lens = len(grid) // 2
        top = grid[:lens]
        a = [i[:lens] for i in top]
        b = [i[lens:] for i in top]
        bottom = grid[lens:]
        c = [i[:lens] for i in bottom]
        d = [i[lens:] for i in bottom]
        return a, b, c, d
# @lc code=end
