# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"
def generate(numRows):

    result=[]
    def generate_row(nums):
        # 1
        line=[]
        for index in range(nums):
            if index == 0 or index == nums-1:
                line.append(1)
            else:
                line.append(result[nums-2][index-1]+result[nums-2][index])
        result.append(line)
    [generate_row(i) for i in range(1,numRows+1)]
    print(result)

generate(5)