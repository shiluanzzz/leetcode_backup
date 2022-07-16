# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


def solve(points:list):

    points.sort(key=lambda x:x[0])
    print(points)
    nums=1
    now=points[0]
    for item in points[1:]:
        print(now)
        if item[0]>now[1]:
            nums+=1
            now=item
        if item[0]<=now[1] and item[0]>=now[0]:
            now=[item[0],now[1]]

        if item[1]<=now[1]:
            now[1]=item[1]

    return nums

if __name__ == '__main__':
    a=solve([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])
    print(a)