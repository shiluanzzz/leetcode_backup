def solve(start,end):
    # XL -> LX
    # RX -> XR
    # start = "RXXLRXRXL", end = "XRLXXRRLX"
    if len(start) != len(end):
        return False
    n=0
    rs,re=0,0
    ls,le=0,0
    while n<len(start):
        if start[n]=="X":
            n+=1
            continue
        if start[n]=="R":
            rs=find_next(rs,start,"R")
            re=find_next(re,end,"R")
            # R可能被调换到右边 所以start的index》end的
            if rs!="F" and re!="F" and rs<=re:
                n+=1
                continue
            else:
                return False
        if start[n] == "L":
            ls = find_next(ls, start,"L")
            le = find_next(le, end,"L")
            # L可能被调换到右边 所以start的index》end的
            if ls!="F" and le!="F" and ls >= le:
                n += 1
                continue
            else:
                return False
    return True

def find_next(char,str,flag):
    while char < len(str):
        if str[char] == flag:
            return char
        else:
            char += 1
    return "F"

if __name__ == '__main__':
    # a=solve(start = "RXXLRXRXL", end = "XRLXXRRLX")
    a=solve("X","L")
    print(a)
