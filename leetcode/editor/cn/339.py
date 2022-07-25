# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"


def solve(equations:list,values:list,queries:list):
    res=[]

    for item in queries:
        if item[0]==item[1]:
            res.append(-1.0)
        else:
            # in equ
            try:
                res.append(values[equations.index(item)])
                continue
            except:
                pass
            # 倒数
            try:
                res.append(values[equations.index([item[1],item[0]])])
                continue
            except:
                pass

            # 接连相除

def solve2(equations:list,values:list,queries:list):
    eqs=[]
    for each in equations:
        flag=0
        for index,i in enumerate(eqs):
            if each[0] in i:
                if each[0] == i[-1]:
                    eqs[index]+=each[1]
                else:
                    pass
                flag=1
        if not flag:
            eqs.append(each[0]+each[1])
    print(eqs)



if __name__ == '__main__':
    print(solve2(
        [["a","b"],["b","c"],["c","d"],["e","f"],["e","b"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ))