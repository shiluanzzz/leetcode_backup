
# 长按键入
class Solution:
    def isLongPressedName(self, name, typed):

        # 1. typed中不能出现多余的字符。
        if set(typed)!=set(name):
            return False
        # name中的字符至少要出现那么多次。

        # 打的第一个字符肯定要一样阿
        if name[:1]!=typed[:1]:
            return False

        # 忘了顺序也要一样- - 只能用双指针了。
        # 输入完毕后就不能有多的字符了。 所以还要加上p==len(typed)的限定条件
        # 可以有多的字符，但是后面的字符只能跟最后一个一样
        # 重复的应该是一样的字符
        # 第一个字符应该一样
        q,p=0,0
        while q<len(name) and p<len(typed):
            if name[q] == typed[p] :
                q+=1
                p+=1
            elif typed[p]==name[q-1]:
                p+=1
            else:
                return False
        # print(q,p)
        if q==len(name) :
            # name全在，而且最后没有多余的字符或者多余的字符都等于name的最后一个字符
            if p==len(typed) or set(typed[p-1:]) == set(name[-1]):
                return True
            else:
                return False
        else:
            return False
        # nums_dict={}
        # for i in name:
        #     nums_dict.setdefault(i,0)
        #     nums_dict[i]+=1
        # for k,v in nums_dict.items():
        #     if typed.count(k) < v:
        #         return False
        # return True

a=Solution().isLongPressedName("zlexya",
                               "aazlllllllllllllleexxxxxxxxxxxxxxxya")
print(a)