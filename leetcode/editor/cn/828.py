# 创建时间:2022-09-06 09:35:38
import collections

# leetcode submit region begin(Prohibit modification and deletion)
import random


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)

        # ---- 某个字母，出现的index
        c_i = [[] for _ in range(26)]
        for i, c in enumerate(s):
            ID = ord(c) - ord('A')
            c_i[ID].append(i)

        res = 0
        for idxs in c_i:
            for i in range(len(idxs)):
                mid = idxs[i]
                l = idxs[i - 1] if 0 <= i - 1 else -1
                r = idxs[i + 1] if i + 1 < len(idxs) else n
                cur = (mid - l) * (r - mid)
                res += cur
        return res

    def uniqueLetterString_M(self, s: str) -> int:
        # 枚举 滑窗复用上一次的结果
        res = dict()
        ans = 0
        for L in range(1, len(s) + 1):
            for i in range(0, len(s) - L + 1):
                res.setdefault(i, [0] * 27)
                idx = ord(s[i + L - 1]) - ord('A')
                if res[i][idx] == 0:
                    res[i][-1] += 1
                elif res[i][idx] == 1:
                    res[i][-1] -= 1
                if res[i][-1] < 0:
                    print(L, i, s[i + L - 1], res[i])
                res[i][idx] += 1
                ans += res[i][-1]
                # res[i][s[i]] += 1
                # ans += len([k for k, v in res[i].values() if v == 1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    ok = """
    "ABC"
    "ABA"
    """
    # params = """
    # "LEETCODE"
    # "ASDAJKSHDJKHASKJHDJKASKJDHKASKJHDKASGHJDGHJASGDHKJFASGHJKDFHASJGDHGASJGDHJKASGDJKHGASHJDFHJASFDGHJ"
    # """
    params = "".join([random.choice("QWERTYUIOPASDFGHJKLZXCVBNM") for _ in range(10000)])
    from leetcode import tools

    Solution().uniqueLetterString(params)
    tools.test_func_batch(Solution().uniqueLetterString, params)
