# 895.最大频率栈
# 创建时间: 2022-08-05 15:01:51

# leetcode submit region begin(Prohibit modification and deletion)
import collections


class FreqStack:

    def __init__(self):
        self.cnt = collections.defaultdict(int)
        self.freq = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # dict 计数
        f = self.cnt[val] + 1
        self.cnt[val] = f
        self.freq[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        res = self.freq[self.max_freq].pop()
        self.cnt[res] -= 1
        if len(self.freq[self.max_freq]) == 0:
            self.max_freq -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# leetcode submit region end(Prohibit modification and deletion)


# main
if __name__ == "__main__":
    import sys

    sys.path.append("D:\\project\\PyProject\\leetcode_record\\")
    import tools

    tools.test_func(Solution().xxx)
