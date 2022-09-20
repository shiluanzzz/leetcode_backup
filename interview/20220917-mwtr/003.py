# _ = input()
# num1 = [int(i) for i in input().split(" ")]
# num2 = [int(i) for i in input().split(" ")]
num1 = [3, 4]
num2 = [2, 5, 1]
n = len(num1) + len(num2)
set1, set2 = set(num1), set(num2)
ans = 0
target = 1
while target < n:
    if target in set1:
        while num1[-1] != target:
            set1.remove(num1[-1])
            set2.add(num1[-1])
            num2.append(num1.pop())
            ans += 1
        num1.pop()
    else:
        while num2[-1] != target:
            set2.remove(num2[-1])
            set1.add(num2[-1])
            num1.append(num2.pop())
            ans += 1
        num2.pop()
    ans += 1
    target += 1

print(ans + 1)
