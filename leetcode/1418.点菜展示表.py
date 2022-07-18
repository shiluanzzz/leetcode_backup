#
# @lc app=leetcode.cn id=1418 lang=python3
#
# [1418] 点菜展示表
#

# @lc code=start
import collections


class Solution:
    # TODO 没仔细读题
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        h=collections.defaultdict(list)
        food = collections.defaultdict(int)
        for each in orders:
            if each[2] not in food:
                food[each[2]]=len(food)
            l=h[each[1]]
            while len(l)-1 < food[each[2]]:
                l.append(0)
            l[food[each[2]]]+=1
        top=[]
        for k,v in food.items():
            top.insert(v,k)
        top.insert(0,"Table")
        ans=[]
        for k,v in h.items():
            t=[str(k)]+[str(i) for i in v]
            ans.append(t)
        ans.sort(key=lambda x:x[0])
        ans.insert(0,top)
        return ans

# @lc code=end
print(Solution().displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))


