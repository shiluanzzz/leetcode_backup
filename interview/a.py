


def solve(y,m,d,h,mm,s,dd):
    month = [31, 28, 31, 30, 31, 20, 31, 31, 30, 31, 30, 31]
    # print(len(month))
    flag=dd
    # new s,m,h
    s,flag=(s+flag)%60,(s+flag)//60
    mm,flag=(mm+flag)%60,(mm+flag)//60
    h,flag=(h+flag)%60,(h+flag)//60
    # new day
    d+=flag
    if y % 4 == 0 or y % 400 == 0 or y % 100 == 0:
        month[1] = 29
    else:
        month[1] = 28

    while d>month[m-1]:
        d-=month[m-1]
        m+=1
        if m//12>0:
            m-=12
            y+=1
        if y%4==0 or y%400==0 or y%100==0:
            month[1]=29
        else:
            month[1]=28
    return "{}:{}:{}:{}:{}:{}".format(y,m,d,h,mm,s)

if __name__ == '__main__':
    a=solve(2019,12,30,22,59,58,9999999)
    print(a)