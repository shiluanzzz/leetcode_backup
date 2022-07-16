
def solve43(num1,num2):

    D={}
    for i in range(0,10):
        D[str(i)]=i
    num1=num1[::-1]
    num2=num2[::-1]
    ans=[0]*(len(num1)+1*len(num2)+1)
    for k,v in enumerate(num2):
        temp=[0]*(k) # 进一位 后面就是 百位相乘 千位相乘
        add=0
        for q in num1:
            temp.append((D[q]*D[v]+add)%10)
            add=(D[q]*D[v]+add)//10
        if add!=0: temp.append(add)
        # 和相加
        add=0
        for k,v in enumerate(temp):
            ans[k],add=(ans[k]+v+add)%10,(ans[k]+v+add)//10
        if add!=0:
            ans[len(temp)]=add
    ans=ans[::-1]
    r=""
    begin=0
    for k,v in enumerate(ans):
        if v!=0:
            begin=k
            break
        else:
            begin+=1
    if begin==len(ans):
        return "0"
    for i in ans[begin:]:
        r+=str(i)
    # print(r)
    return r

if __name__ == '__main__':
    solve43("0","0")
    solve43("9","9")
    solve43("12342231231231314512341","842")