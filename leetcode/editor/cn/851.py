# 851. 喧闹和富有


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import heapq


class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        dag,degree=collections.defaultdict(set),[0]*len(quiet)
        for a,b in richer:
            dag[a].add(b)
            degree[b]+=1
        queue=collections.deque([k for k,i in enumerate(degree) if i==0])
        ans=[i for i in range(len(quiet))]
        while len(queue)!=0:
            item=queue.popleft()
            for each in dag[item]:
                # 这里不是item 应该是ans[item]
                # 应为可能存在多重的叠加关系
                if quiet[ans[item]]<quiet[ans[each]]:
                    ans[each]=ans[item]
                degree[each]-=1
                if not degree[each]:
                    queue.append(each)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]))
