# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

def romanToInt(s: str) -> int:
    spacial = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    ans = 0
    q, h = 0, 1
    lens = len(s)
    while h < lens + 1:
        # 判断是否符合特殊条件
        # if q + 1 == h and s[q:h] in ['I', 'X', 'C'] and h + 1 < lens + 1 and s[q:h + 1] in spacial.keys():
        if  s[q:h] in ['I', 'X', 'C']  and s[q:h + 1] in spacial.keys():
            ans += spacial.get(s[q:h + 1])
            print(spacial.get(s[q:h + 1]))
            q = h + 1
            h = h + 2
        else:
            ans += d.get(s[q:h])
            print(d.get(s[q:h]))
            q += 1
            h += 1
    return ans


print("ans", romanToInt('IV'))
