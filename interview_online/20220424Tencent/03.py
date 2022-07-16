n=int(input())
flag=input()
# 1000101
# 1234567
ans=0
for i,v in enumerate(flag):
    if v=='0':continue
    ans+=(i+1)
defend=ans
attack=0
for i,v in enumerate(flag):
    i+=1
    if v=='1':
        attack+=i
    else:
        defend-=i
    # print(i,attack,defend)
    ans=min(ans,abs(defend-attack))
print(ans)