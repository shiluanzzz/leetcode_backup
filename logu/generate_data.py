
import random
def gen1(n):
    # n 行金字塔数据
    with open("gen1.txt",'w') as f:
        f.write(str(n)+"\n")
        for i in range(1,n+1):
            for _ in range(i):
                f.write(str(random.randint(0,9)))
                f.write(" ")
            f.write("\n")
    print("end")

gen1(1000)