# 3个任务分给5个人


# from asyncore import read


def dfs(remain,index):
    if remain<0 or index>5:return 0
    if remain==0:
        return 1
    return dfs(remain-1,index+1)+dfs(remain,index+1)+dfs(remain-2,index+1)+dfs(remain-3,index+1)

# print(dfs(3,1)0#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param text_source string字符串 原始输入
# @return string字符串
#
from cgi import test
import heapq
class Solution:
    def char_and_num_return(self , text_source ):
        # write code here
        text_source=text_source.strip()
        left=0
        ans=[]
        temp=[]
        for i in range(len(text_source)+1):
            if i==len(text_source) or text_source[i]==' ':
                ss=text_source[left:i]
                left=i+1
                if ss:
                    if ord(ss[0])>=ord('1') and ord(ss[0])<=ord('9'):
                        heapq.heappush(temp,int(ss))
                    else:
                        ans.append(ss)
        ans.extend([str(i) for i in heapq.nsmallest(len(temp),temp)])
        return " ".join(ans)

print(Solution().char_and_num_return("xb cc dd ee 1 2 5 10"))
print(Solution().char_and_num_return("abc dad fsad fas 10"))
print(Solution().char_and_num_return("avv 1 2 3 4 5 6 dfa"))