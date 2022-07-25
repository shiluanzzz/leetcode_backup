# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


def solve(str,nums):
    if len(str)==nums:
        return "0"

    # 从前往后找最小的nums个数拿掉
    # 用栈先进后出
    stack=[]
    i=0
    count=0
    while i <len(str) and count<nums:
        if stack:
            if int(str[i])<int(stack[-1]):
                stack.pop(-1)
                count+=1
            else:
                stack.append(str[i])
                i+=1
        else:
            stack.append(str[i])
            i+=1
    while count<nums:
        stack.pop(-1)
        count+=1
    stack.extend(str[i:])
    while len(stack)>1 and stack[0]=="0":
        stack.pop(0)

    return "".join(stack)
    # print(stack)
    # print(str[i:])

if __name__ == '__main__':
    # a=solve("1432219",3)
    # print(a)
    print(solve("112",1))

    print(solve("112",2))
    print(solve("100000120000",2))

    print(solve("100000120000",3))
