# 成对的69匹配序列定义为：
# 1、 空串""是一个成对的69序列；
# 2、如果"X"和"Y"是成对的69序列，那么"XY"也是成对的69序列；
# 3、如果"X"是一个成对的69序列，那么"6X9"也是一个成对的69序列；
# 4、每个成对的69序列都可以由以上规则生成。 例如，"", "69", "6699", "6969"都是成对的。
# 现在给出一个序列S，允许你的操作是： 在S的开始和结尾出添加一定数量的6或者9，使序列S变为一个成对的69序列。输出添加最少的6或者9之后成对的69序列是什么。

class Solution:
    def Paired69(self , S ):
        # write code here
        if S=="":return S
        top,bottom="",""
        stack=[]
        for i in S:
            if len(stack) and stack[-1]!=i:
                stack.pop()
            else:
                stack.append(i)
        