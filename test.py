from random import random
import re
from tkinter.messagebox import NO

p="hi !, test . char?';"
np=re.split(r"([ ,.!?';])", p.lower())
# ['hi', ' ', '', '!', '', ',', '', ' ', 'test', ' ', '', '.', '', ' ', 'char', '?', '', "'", '', ';', '']
# ['hi', '', '', '', 'test', '', '', 'char', '', '', '']
print(np)
import random
import heapq
a=[]
class Node:
    def __init__(self) -> None:
        Node.val=random.randint(0,9)

for _ in range(10):
    t=Node()
    heapq.heappush(a,[t.val,t])

while a:
    t=heapq.heappop(a)
    print(t[0])