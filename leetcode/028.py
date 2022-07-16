# -*- coding:utf-8 -*-
# __author__ = "shitou6"

# 给定一个 haystack 字符串和一个 needle 字符串，
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        q=0
        while(q+len(needle)<=len(haystack)):
            p=q
            flag=0
            for i in needle:
                if i==haystack[p]:
                    p,flag=p+1,flag+1
                else:
                    flag=0
                    break
            if flag==len(needle):
                return q
            else:
                q+=1
        return -1
    def strStr2(self,haystack:str,needle:str)->int:

        # 偏移表
        def calShiftMat(st):
            dic={}
            for i in range(len(st)-1,-1,-1):#倒序遍历
                if not dic.get(st[i]): # 只取最大的偏执位置
                    dic[st[i]]=len(st)-i
            dic['ot']=len(st)+1 # 其他情况
            return dic
        # special case
        if len(needle)==0:return 0
        if len(needle)>len(haystack):return -1

        #
        dic=calShiftMat(needle)
        idx=0
        while(idx+len(needle)<=len(haystack)):
            str_cut=haystack[idx:idx+len(needle)]

            if str_cut==needle:
                return idx
            else:
                # 边界处理
                if idx+len(needle)>=len(haystack):
                    return -1
                next_c=haystack[idx+len(needle)] #profund understand
                if dic.get(next_c):
                    idx+=dic[next_c]
                else:
                    idx+=dic['ot']
        return -1 if idx+len(needle) >= len(haystack) else idx

s=Solution()
print(s.strStr2("mississippi",
                "issi"))