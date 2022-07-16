# 杨辉三角 输入一个整数N 输出N出现的第几个位置
N=int(input())
hash={}
def table(max_n):
    hash[1]=1
    num=[1,1]
    count=1
    flag=True
    while flag:
        # print(num)
        count+=len(num)
        temp=[1]
        for i in range(1,len(num)):
            v=num[i-1]+num[i]
            if v not in hash:
                hash[v]=count+len(temp)+1
                if v>max_n:
                    flag=False
            temp.append(v)
        temp.append(1)
        num=temp
    print(hash)
def solve(n):
    if n==1:return 1
    num=[1,1]
    count=1
    while True:
        print(num)
        count+=len(num)
        temp=[1]
        for i in range(1,len(num)):
            v=num[i-1]+num[i]
            if v==n:
                return count+len(temp)+1
            temp.append(v)
        temp.append(1)
        num=temp
print(table(N))