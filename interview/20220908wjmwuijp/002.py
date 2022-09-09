#
import functools


@functools.cache
def solve(n:int):
    # 偶数 n/2
    # 奇数 2n+2 2n-2 或者
    if n == 1: return 0
    if n % 2 == 0:
        return solve(n // 2)+1
    else:
        return min(solve(2 * n + 2), solve(2 * n - 2))+1

if __name__ == '__main__':
    from leetcode import tools
    params="""
    10
    10000
    523
    8
    4
    3
    """
    tools.test_func_batch(solve,params)