# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

def solve(matrix):
    x,y=0,0
    res=[]
    up,right,left,down=0,len(matrix[0]),-1,len(matrix)
    count=0
    while count<right*down:
        while y<right:
            res.append(matrix[x][y])
            y+=1
            count+=1
        y-=1
        x+=1
        while x<down:
            res.append(matrix[x][y])
            x+=1
            count+=1
        x-=1
        y-=1
        while y>left:
            res.append(matrix[x][y])
            y-=1
            count+=1
        y+=1
        x-=1
        while x>up:
            res.append(matrix[x][y])
            x-=1
            count+=1
        x+=1
        y-=1
        up,right,left,down=up+1,right-1,left+1,down-1

    print(res)





print(solve([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
