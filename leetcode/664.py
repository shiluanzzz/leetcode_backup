

def solve(s):
    i,n=1,len(s)
    now_print=s[0]
    count=1
    while i<n:
        if s[i]!=s[0] and s[i]!=now_print:
            now_print=s[i]
            count+=1
        if s[i]!=now_print:
            now_print=s[i]
        i+=1
    return count

print(solve("abc"))
print(solve("ababab"))

