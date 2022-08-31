# 创建时间:2022-08-31 11:14:41
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    TODO 根据可能读到的字符类型，做一个状态机的转化。
    cr:
    字符串处理的题目往往涉及复杂的流程以及条件情况，如果直接上手写程序，一不小心就会写出极其臃肿的代码。
    因此，为了有条理地分析每个输入字符的处理方法，我们可以使用自动机这个概念：
    我们的程序在每个时刻有一个状态 s，每次从序列中输入一个字符 c，并根据字符 c 转移到下一个状态 s'。这样，我们只需要建立一个覆盖所有情况的从 s 与 c 映射到 s' 的表格即可解决题目中的问题。
    """

    def myAtoi(self, s: str) -> int:


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    params = """
    
    """
    from leetcode import tools

    tools.test_func_batch(Solution().myAtoi(), params)
