# 1346. 跳跃游戏 IV


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        hash=collections.defaultdict(list)
        for i,v in enumerate(arr):
            hash[v].append(i)

        def trip(index,count):
            if index==0:return count
            ans=-1
            for i in hash[arr[index]]:
                if i<index:
                    ans=trip(i,count+1)
                    break
            if index+1<len(arr):
                t=trip(index+1,count+1)
                ans=min(ans,t)
            if index-1>0:
                t=trip(index-1,count+1)
                ans=min(ans,t)
            return ans
        return trip(len(arr)-1,0)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404]))

