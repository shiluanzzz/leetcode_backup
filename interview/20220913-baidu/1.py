# baidu型字符串
import random


# ss = input()

def solve(ss):
    y = ['a','e','i','o','u']
    y = set(y)
    ans = 0
    for i in range(0,len(ss)-4):
        if len(set(ss[i:i+5])) != 5 : continue
        if ss[i] not in y and ss[i+1] in y and ss[i+2] in y and ss[i+3] not in y and ss[i+4] in y:
            ans+=1
    print(ans)

if __name__ == '__main__':
    from leetcode.tools import test_func
    ss="".join([random.choice("qwertyuiopasdfghjklzxcvbnm") for _  in range(200000)])
    print(len(ss))
    solve(ss)