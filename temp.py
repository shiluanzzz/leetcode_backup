
from collections import defaultdict

wordList=["lest","leet","lose","code","lode","robe","lost"]
buckets = defaultdict(list)
for word in wordList:
    for i in range(4):
        match = word[:i] + '_' + word[i+1:]
        buckets[match].append(word)
    
print(buckets)
 
a=eval(input())
print(len(set(a)))
print(len(a))