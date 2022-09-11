# 创建时间:2022-09-09 08:19:32

# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = collections.deque([])
        for v in logs:
            if v == "../":
                if len(stack):
                    stack.pop()
            elif v == "./":
                pass
            else:
                stack.append(v[:-1])
        print(stack)
        return len(stack)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    ["./","../","./"]
    """
    from leetcode import tools

    tools.test_func_batch(Solution().minOperations, params)
