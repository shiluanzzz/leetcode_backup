

def solve(asteroids:list):
    n=len(asteroids)
    if n<=1:
        return asteroids

    i=0
    flag = asteroids[0]>0
    if flag:
        while i<len(asteroids)-1:
            if asteroids[i+1]<0:
                if abs(asteroids[i+1])>abs(asteroids[i]):
                    asteroids.pop(i)
                    i+=1
                elif asteroids[i+1]+asteroids[i]==0:
                    asteroids.pop(i)
                    asteroids.pop(i)
                else:
                    asteroids.pop(i+1)
            else:
                i+=1
    return asteroids

def solve2(s):
    if len(s)<2:
        return s
    i=0
    while i<len(s)-1:
        if s[i]>0 and s[i+1]<0:
            if s[i]+s[i+1]==0:
                s.pop(i)
                s.pop(i)
                i=i-1 if i>0 else i
            elif s[i]+s[i+1]<0:
                s.pop(i)
                if i>0:
                    i-=1
                else:
                    i+=1
            else:
                s.pop(i+1)
        else:
            i+=1
    return s

def solve3(s):
    # use stack
    res=[]
    i=0
    while i<len(s):
        if len(res)==0 or s[i]>0:
            res.append(s[i])
        else:
            t=res.pop(-1)
            
print(solve2([1,4,5,-6,]))
print(solve2([1,4,5,-8,9,-10]))
print(solve2([-8,5,-4,3,5,]))
print(solve2([1,1,-1,-2]))