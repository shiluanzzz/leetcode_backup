# # -*- coding:utf-8 -*-
# # __author__ = "shiluanzzz"
# # 最长的回文子串
# 
# # 把子串的下半部分转置在跟前半部分对比。
# 
# import time
# 
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         indexs=yield_sub_inedx(len(s))
#         for q,p in indexs:
#             # print(q,p)
#             if func2(s,q,p) :
#                 return s[q:p]
#         return s[0]
# 
#     def longestPalindrome1(self, s: str) -> str:
#         indexs=yield_sub_inedx(len(s))
#         for q,p in indexs:
#             # print(q,p)
#             if s[q:p]==s[q:p:-1]:
#                 return s[q:p]
#         return s[0]
#     # 一轮遍历 来自网络题解
#     def longestPalindrome2(self, s: str) -> str:
#         if not s: return ""
#         length = len(s)
#         if length == 1 or s == s[::-1]: return s
#         max_len,start = 1,0
#         for i in range(1, length):
#             even = s[i-max_len:i+1]
#             odd = s[i-max_len-1:i+1]
#             print("i:{} even:{} odd:{}".format(i,even,odd))
#             if i - max_len - 1 >= 0 and odd == odd[::-1]:
#                 start = i - max_len - 1
#                 max_len += 2
#                 continue
#             if i - max_len >= 0 and even == even[::-1]:
#                 start = i - max_len
#                 max_len += 1
#                 continue
#         return s[start:start + max_len]
# 
# def func2(s,b,e):
#     bb,ee=b,e-1
#     while bb<=ee:
#         if s[bb]!=s[ee]:
#             return 0
#         else:
#             bb+=1
#             ee-=1
#     return 1
# 
# 
# # 迭代出固定长度的子串下标
# # [x,x,x,x]
# # [0:4],[0,3],[1,4],[2,4],[0,2],[1,3],[2,4] ...
# def yield_sub_inedx(lens):
#     # lens=lens-1
#     now_lens=lens
#     i=0
#     # while i+now_lens<=lens and now_lens!=0:
#     while True:
#         yield i,i+now_lens
#         if i+now_lens == lens and now_lens !=0:
#             now_lens-=1
#             i=0
#         elif now_lens==0:
#             break
#         else:
#             i+=1
# 
# t=time.time()
# s=Solution()
import time

ss="twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"

def long_str(ss:str):

    n = len(ss)
    if n==0: return ""
    if judge(ss) : return ss
    max_result=""
    # max_len = n-1
    # while max_len>1:
    for max_len in range(1,n)[::-1]:
        for i in range(n):
            if i+max_len >n:
                break
            elif judge(ss[i:i+max_len]):
                max_result = ss[i:i+max_len]
                return max_result
    return ""


def judge(ss):
    print("judge ",ss)
    if ss ==ss[::-1]:
        return True
    else:
        return False

print(long_str(ss))