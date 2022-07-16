# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"#

# 冒泡

def mySort(data):

    i,n=0,len(data)
    while i<n:
        print(data[i],end=" ")
        k=i+1
        while k<n:
            if data[k]<data[i]:
                data[i],data[k]=data[k],data[i]
            k+=1
        print(data)
        i+=1
    print(data)

if __name__ == '__main__':
    print(atio("[2,3,1]"))
    mySort([2,8,3,1,7,10,4,9,6])