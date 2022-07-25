import collections
from opcode import haslocal
from this import d

solve=collections.defaultdict(int)
has=set(["aba","aab","aaa","c"])
solve[3]=len(has)
count=4
def get(count):
    global has
    add_temp=set()
    for i in has:
        add_temp.add('a'+i)
        add_temp.add(i+'a')
    has=add_temp
    # print(has)
    return len(has)
for i in range(4,10):
    print(i,get(i))
print(solve)