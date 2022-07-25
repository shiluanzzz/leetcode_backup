import time


def solve(i):
    if i==0:return [1]
    # item :i+1
    result=[]
    # solve middle result

    if i%2==0:n=i/2
    else: n=(i-1)/2+1
    n=int(n)

    for each in range(i+1):
        if each == 0 or each ==i:
            result.append(1)
        else:
            result.append(dp(i,each))

    # result.extend(result[::-1][:i+1-n])
    return result
def dp(line,index):
    if line==0 : return 1
    else:
        if index==0 or index == line : return 1
        else :
            return dp(line-1,index-1)+dp(line-1,index)


def generate(line):
    old = []
    for each in range(line+1):
        new = []
        for i in range(each+1):
            # print(each,i)
            if i==0 or i == each:
                new.append(1)
            else:
                new.append(old[i]+old[i-1])

        old=new
    return old
if __name__ == '__main__':
    print(generate(33))