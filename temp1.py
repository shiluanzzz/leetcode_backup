def getSign(a):
    if a >=0:
        return''
    else:
        return'-'
def getString(n,x):
    #n为待转换的十进制数，x为机制，取值为2-16
    a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    ans=""
    for i in b:
        ans+=str(a[i])
    return ans
a = int(input())
b = int(input())
mark = getSign(a)
bitString = getString(abs(a), b)
print(mark + bitString)