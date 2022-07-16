

def solve71(path):
    child=[]
    i=1
    if path[-1]!='/':path=path+'/'
    while len(path) and i<len(path):
        if path[i]=="/" and i!=1:
            str = path[1:i]
            while len(str) and str[0] == "/":
                str = str[1:]
            if len(str):
                # if str[0]=="/":str=str[1:]
                if str=="..":
                    child=child[:-1]
                elif str!=".":
                    child.append(str)
            path=path[i:]
            i=1
        else:
            i+=1
        print(child)
    ans=""
    for each in child:
        ans=ans+'/'+each
    if ans:
        return ans
    else:
        return "/"

if __name__ == '__main__':
    # print(solve71("/a/./b/..//c//dd/"))
    print(solve71("/a//b////c/d//././/.."))

