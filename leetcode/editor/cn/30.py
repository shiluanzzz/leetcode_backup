# 创建时间:2022-08-29 11:30:48


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # 字符串s中的字串长度不一定等于words中的子串长度
        if len(words) * len(words[0]) > len(s):
            return []
        hash = set(words)
        ans = []
        for i in range(0, len(s) - len(words) * len(words[0]) + 1):
            if s[i:i+len(words[0])] not in hash:
                continue
            counter, total, history = collections.Counter(words), len(words), collections.deque()
            for j in range(i, len(s), len(words[0])):
                cur = s[j:j + len(words[0])]
                if counter[cur] > 0:
                    counter[cur] -= 1
                    total -= 1
                else:
                    break
            if total == 0: ans.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    params = """
    "barfoofoobarthefoobarman"
    ["bar","foo","the"]
    "wordgoodgoodgoodbestword"
    ["word","good","best","good"]
    "lingmindraboofooowingdingbarrwingmonkeypoundcake"
			["fooo","barr","wing","ding","wing"]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().findSubstring, params)
