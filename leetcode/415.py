class Solution:
    # 拆分后相加
    def addStrings(self, num1: str, num2: str) -> str:
        def chai(num1):
            num1=list(num1)
            # 拆分字符串
            num1_true=0
            for i in num1:
                i=ord(i)-ord('0')
                num1_true+=i
                num1_true*=10
            num1_true/=10
            return  num1_true
        return str(int(chai(num1)+chai(num2)))
        # 输入：溢出了- -！淦
        # "9333852702227987"
        # "85731737104263"
        # 输出：
        # "9419584439332252"
        # 预期结果：
        # "9419584439332250"
    # 双指针
    def addStrings2(self, num1: str, num2: str) -> str:
        # n1=len(num1)-1
        # n2=len(num2)-1
        # add=0 更高级的写法
        n1,n2,add=len(num1)-1,len(num2)-1,0
        ss=""
        #双指针只能是从后往前加！
        # 这里的while 用and处理很麻烦，不如用or 当遍历完了以后用0填充就行
        while n1>=0 or n2>=0:
            i1=int(num1[n1]) if n1>=0 else 0
            i2=int(num2[n2]) if n2>=0 else 0
            tem=i1+i2+add
            add=tem//10
            ss=str(tem%10)+ss

            # n1-=1
            # n2-=1 更高级的写法
            n1,n2=n1-1,n2-1
        return "1"+ss if add else ss
    def addStrings3(self, num1: str, num2: str) -> str:
        pass



S=Solution()

print(S.addStrings2('98','9'))