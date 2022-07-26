#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
# @lc code=start
import collections


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if target == "0000": return 0
        if target in deadends or "0000" in deadends: return -1
        deadends = set(deadends)

        def num_next(i: str):
            return "0" if i == "9" else str(int(i) + 1)

        def num_prev(i: str):
            return "9" if i == "0" else str(int(i) - 1)

        def get_state(s):
            # s:0000
            s = list(s)
            for i in range(4):
                num = s[i]
                s[i] = num_next(num)
                yield "".join(s)
                s[i] = num_prev(num)
                yield "".join(s)
                s[i] = num

        q = collections.deque([("0000", 0)])
        visited = {"0000"}
        while q:
            item, num = q.popleft()
            for state in get_state(item):
                if state in deadends or state in visited:
                    continue
                if state == target:
                    return num + 1
                q.append((state, num + 1))
                visited.add(state)
        return -1

    def openLock_1(self, deadends: list[str], target: str) -> int:
        # @review：用广度搜索枚举所有的可能情况
        # @TODO 写法还能优化一下 应该使用set,yield
        if target == "0000": return 0
        if target in deadends or "0000" in deadends: return -1
        dead = {i: True for i in deadends}
        seached = {}
        queue = [("0000", 0)]
        next_key = {str(i): str(i + 1) for i in range(0, 9)}
        next_key["9"] = "0"
        pre_key = {str(i): str(i - 1) for i in range(1, 10)}
        pre_key["0"] = "9"
        while queue:
            item, num = queue.pop(0)
            for i in range(4):
                t = list(item)
                t[i] = next_key[t[i]]
                next_item = "".join(t)
                if next_item == target:
                    return num + 1
                if next_item in dead:
                    continue
                if next_item not in seached:
                    queue.append(("".join(t), num + 1))
                    seached[next_item] = 1

            for i in range(4):
                t = list(item)
                t[i] = pre_key[t[i]]
                next_item = "".join(t)
                if next_item == target:
                    return num + 1
                if next_item in dead:
                    continue
                if next_item not in seached:
                    queue.append(("".join(t), num + 1))
                    seached[next_item] = 1
        return -1


# @lc code=end


# import sys
# sys.path.append("C:\\project\\PyProject\\leetcode_record\\")
# import tools
# tools.test_func(Solution().openLock,"..\\..\\..\\in.txt","..\\..\\..\\out.txt")
