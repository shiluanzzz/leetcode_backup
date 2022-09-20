import collections
import functools

n = int(input())

num_a = [int(i) for i in input().split(" ")]
num_b = [int(i) for i in input().split(" ")]
vals = [int(i) for i in input().split(" ")]


# 3
# 1 1
# 2 3
# 1 1 2

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.child = []


def solve(n, num_a, num_b, vals):
    trees = collections.defaultdict(TreeNode)
    for i in range(1, n + 1):
        trees[i] = TreeNode(vals[i - 1])
    for i in range(len(num_a)):
        trees[num_a[i]].child.append(trees[num_b[i]])

    @functools.cache
    def min_node(root: TreeNode):
        if not root.child:
            return root.val
        return min(root.val, min([min_node(node) for node in root.child]))

    for i in range(1, n):
        v = trees[i]
        if len(v.child) != 0 and v.val < min_node(v):
            return i
    return -1


print(solve(n, num_a, num_b, vals))
