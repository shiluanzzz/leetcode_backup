


def solve(nums):
    if len(nums)==1:return 0
    result=[]
    i,j=0,nums[0]
    count=0
    while j<len(nums):
        print(i,j)
        temp=j
        if i!=j:
            j=max([nums[k]+k for k in range(i+1,j+1)])
            i=temp
        else:
            i=j
            j=nums[i]+i

        count+=1
    return count

if __name__ == '__main__':
    print(solve([2,3,1,1,4]))
    print(solve([0]))