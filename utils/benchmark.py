import time


import sys
sys.setrecursionlimit(9999)

def test1():
    # 递归传递和引用传递的速度比较
    test_count=2666
    def func1(i,count,ans):
        if i>=count:
            return ans
        else:
            ans.append("1")
            return func1(i+1,count,ans)
    t1=time.time()
    print("开始测试",end=" ")
    func1(0,test_count,[])
    print("递归传值，耗时",time.time()-t1)

    ans=[]
    def func2(i,count):
        if i>=count:
            return ans
        else:
            ans.append("1")
            return func1(i+1,count,ans)
    t1=time.time()
    func2(0,test_count)
    print("外部值，耗时", time.time() - t1)
def test_join_str():
    max_count=2444
    s=""
    begin_time=time.time()
    for i in range(max_count):
       s+=str(i)
    print("迭代拼接",time.time()-begin_time)

    def func1(i,ans:str):
        if i>=max_count:
            return ans
        return func1(i+1,ans+str(i))
    begin_time=time.time()
    func1(0,"")
    print("递归拼接",time.time()-begin_time)
    def func2(i,ans):
        if i>=max_count:
            return ans
        ans.append(str(i))
        return func2(i+1,ans)
    begin_time=time.time()
    a=func2(0,[])
    s="".join(a)
    print("递归拼接,数组",time.time()-begin_time)

if __name__ == '__main__':
    # test1()
    test_join_str()