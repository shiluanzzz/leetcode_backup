
# 按马走
def solve_1(x,y):
    k={}
    # 马 x+-2 y+-1
    def dp(x,y,count):
        key="{}-{}".format(x,y)
        k.setdefault(key,-1)
        if k["{}-{}".format(x,y)]!=-1:
            return k["{}-{}".format(x,y)]
        if x<0 or x>400 or y<0 or y>400:
            return float("inf")
        if x==1 and y==1:
            k["{}-{}".format(x,y)]=count
            return count
        else:
            return min(
                dp(x+2,y+1,count+1),dp(x-2,y-1,count+1),dp(x+2,y-1,count+1),dp(x-2,y+1,count+1)
            )
    return dp(x,y,0)

def solve2_1(nums,n,k):
    assert len(nums)==n
    # 从数组中选k个数取平均值然后 计算剩下的最大最小差值


if __name__ == '__main__':
    solve_1(2,1)