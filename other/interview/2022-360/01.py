import collections

dic=collections.defaultdict(int)
s=input()
for lens in range(1,len(s)+1):
    for i in range(0,len(s)-lens+1):
        ss=s[i:lens+i]
        dic[ss]+=1
        # print(ss)
print(max(dic.values()))