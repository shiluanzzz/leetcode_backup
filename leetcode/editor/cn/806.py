
def solve(widths,s):
    line,count=0,0
    n=0
    while n<len(s):
        each=s[n]
        if count + widths[ord(each)-ord('a')]>100:
            line+=1
            count=0
        else:
            count+=widths[ord(each)-ord('a')]
            n+=1
    return [line,count]