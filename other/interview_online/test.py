
def generate(num,count):
    for i in num:
        for c in range(count):
            # 只有在取数据的时候才会产生数据
            # 而不是一次性扩充count倍返回数据
            yield i

for k in generate([1,2,3],10000):
    # 在这里用数据
    print(k)

