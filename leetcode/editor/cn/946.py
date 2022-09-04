# 创建时间:2022-08-31 10:30:27	获取当前时间
# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        从popped判断，如果下一个弹出栈的元素是在上一个弹出元素的输入的左边或者右边那就符合规则.

        上面的想法有点缺陷:
        1.对于下一个出栈的元素，在入栈顺序上，必须紧挨上一个入栈的元素
        2.对于下一个出栈的元素，可以是入栈顺序的最后一个元素

        错了[4,0,3,1,2]
			[4,1,3,0,2]
		直接模拟入栈出栈不就行了？
		p是验证栈，便利poped,如果当前的元素在p的末尾，直接出栈，
		如果不在就从pushed里模拟往验证栈p中送进入，直到出现了当前的元素
        """
        p = collections.deque()
        for v in popped:
            if len(p)>0 and p[-1] == v:
                p.pop()
            else:
                while len(pushed) > 1 and pushed[0] != v:
                    p.append(pushed.pop(0))
                if len(pushed) > 0:
                    # 把v探出栈
                    pushed.pop(0)
                else:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    params = """
    [1,2,3,4,5]
    [1,2,3,4,5]
    [1,2,3,4,5]
    [4,5,3,2,1]
            [1,2,3,4,5]
            [4,3,5,1,2]
            [0,2,1]
            [0,1,2]
            [4,0,3,1,2]
			[4,1,3,0,2]
            """
    from leetcode import tools

    tools.test_func_batch(Solution().validateStackSequences, params)
