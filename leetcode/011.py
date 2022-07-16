# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


# 盛最多水的容器

def solve(height:list):
    i,j=0,len(height)-1
    result = 0
    def cal(i,j):
        return min(height[i],height[j])*abs(j-i)
    while i<j:
        new_result = min(height[i],height[j])*abs(j-i)
        if new_result>result:
            result=new_result
        else:
            k=i+1
            while k<j and height[k]<height[i] and height[k]<height[j]:
                k+=1
            if k>=j:
                return result
            else:
                # 离k最近的i,j移动到k位置
                # if k-i > j-k:
                #     j=k
                # else:
                #     i=k
                if cal(k,j)>cal(i,k):
                    i=k
                else:
                    j=k
def solve2(height):
    i,j,res=0,len(height)-1,0
    while i<j:
        res = max(res,min(height[i],height[j])*abs(j-i))
        if height[j]>height[i]:
            i+=1
        else:
            j-=1
    return res
if __name__ == '__main__':

    print(solve2([1,19,6,2,5,4,19,3,7]))
    print(solve2([1,1]))
    print(solve2([4,3,2,1,4]))
    print(solve2([1,2,1]))
    print(solve2([2,3,4,5,18,17,6]))