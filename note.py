import heapq

if __name__ == '__main__':
    list=[]
    heapq.heappush(list,[3,"three"])
    heapq.heappush(list,[1,"one"])
    heapq.heappush(list,[5,"five"])
    print("堆:",list)
    print("访问最小值:",list[0])
    print("访问最大值",heapq.nlargest(1,list)[0])