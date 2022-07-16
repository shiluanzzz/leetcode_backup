# 210. 课程表 II


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indata=[0]*numCourses
        outData=collections.defaultdict(list)
        hash=collections.defaultdict(bool)
        for o,i in prerequisites:
            indata[i]+=1
            outData[o].append(i)
        queue=[]
        for i,v in enumerate(indata):
            if v==0:
                queue.append(i)
                hash[i]=True
        ans=[]
        while len(queue)!=0:
            # print(queue)
            ans.append(queue[0])
            for v in outData[queue[0]]:
                indata[v]-=1
            queue.remove(queue[0])
            for i,v in enumerate(indata):
                if i in hash:continue
                if v==0:
                    queue.append(i)
                    hash[i]=True
        if len(ans)==numCourses:
            return ans[::-1]
        return []

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))