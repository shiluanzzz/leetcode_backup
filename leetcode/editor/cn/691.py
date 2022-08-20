# 691.贴纸拼词
# 创建时间: 2022-08-18 11:58:10

# leetcode submit region begin(Prohibit modification and deletion)
import collections
import os


class Solution:
    def minStickers2(self, stickers: list[str], target: str) -> int:
        # 解法一： BFS + 枚举
        def trans(s):
            ct = collections.Counter()
            for v in s:
                if v in target:
                    ct[v] += 1
            return ct

        # := 用于在表达式内部赋值 if (n:=len(a))>10 这样
        ava = [c for s in stickers if (c := trans(s))]
        visited = {target}
        que = collections.deque([(target, 0)])
        while que:
            item, step = que.popleft()
            if not item: return step
            # 枚举所有的情况
            for each in ava:
                # 枚举所有可选的卡片替换掉字符然后加到队列中
                nex = item
                for k, v in each.items():
                    # nex = nex.replace(k, "", v if v<len(k) else len(k))
                    nex = nex.replace(k, "", v)
                if nex not in visited:
                    que.append((nex, step + 1))
                    visited.add(nex)
        return -1

    def minStickers(self, stickers: list[str], target: str) -> int:
        # 解法2 状态压缩
        def trans(s):
            ct = collections.Counter()
            for v in s:
                if v in target:
                    ct[v] += 1
            return ct

        ticks = [s for i in stickers if (s := trans(i))]
        queue = collections.deque([(0, 0)])
        visited = {0}
        while queue:
            state, count = queue.popleft()
            # 状态位全位1
            if state == int(pow(2, len(target))) - 1:
                return count
            # 遍历可以用的卡片 BFS
            for tick in ticks:
                tick = tick.copy()
                next_state = state
                for i in range(len(target)):
                    if next_state & (1 << i) > 0:
                        # 状态位为1
                        continue
                    if tick[target[i]] > 0:
                        tick[target[i]] -= 1
                        next_state |= (1 << i)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, count + 1))
        return -1


# leetcode submit region end(Prohibit modification and deletion)


# main
if __name__ == "__main__":
    import sys

    # ---
    sys.path.append("D:\\project\\PyProject\\leetcode_record\\leetcode")
    from utils import tools

    # print(os.getcwd())
    os.chdir("D:\\project\\PyProject\\leetcode_record")
    # print(os.getcwd())
    # ---
    tools.test_func(Solution().minStickers2)
