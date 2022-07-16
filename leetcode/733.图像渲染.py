#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
from functools import lru_cache


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        row,col=len(image),len(image[0])
        target=[[sr,sc]]
        target_color=image[sr][sc]
        
        @lru_cache
        def fill(x,y):
            if x<0 or x>row-1:return 
            if y<0 or y>col-1:return
            if image[x][y]==target_color:
                image[x][y]=newColor
                target.append([x-1,y])
                target.append([x+1,y])
                target.append([x,y+1])
                target.append([x,y-1])
            return
        while target:
            t=target.pop()
            fill(t[0],t[1])
        return image
# @lc code=end

print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]],sr = 1, sc = 1, newColor = 2))