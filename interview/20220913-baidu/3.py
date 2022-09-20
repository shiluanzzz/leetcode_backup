import functools

# input_str=[int(i) for i in input().split(" ")]
# n,m=input_str[0],input_str[1]
# grid = [input() for _ in range(n)]

grid = [
    "red",
    "der",
    "rdr"
]
n, m = 3, 3
# r->d e->r d->e error
ban = {
    'r': 'd',
    'e': 'r',
    'd': 'e',
}
ban = {
    k: v for v, k in ban.items()
}
# print(ban)
count = [[float('inf')] * m for _ in range(n)]
count[0][0] = 0


def visited():
    changed = False
    for j in range(m):
        for i in range(n):
            if n == 0 and m == 0:
                continue
            if i > 0 and grid[i - 1][j] != ban[grid[i][j]] and count[i - 1][j] != float('inf') and count[i - 1][j] + 1 < \
                    count[i][j]:
                count[i][j] = count[i - 1][j] + 1
                changed = True
            if j > 0 and grid[i][j - 1] != ban[grid[i][j]] and count[i][j - 1] != float('inf') and count[i][j - 1] + 1 < \
                    count[i][j]:
                count[i][j] = count[i][j - 1] + 1
                changed = True

            if i < n - 1 and grid[i + 1][j] != ban[grid[i][j]] and count[i + 1][j] != float('inf') and count[i + 1][
                j] + 1 < count[i][j]:
                count[i][j] = count[i + 1][j] + 1
                changed = True

            if j < m - 1 and grid[i][j + 1] != ban[grid[i][j]] and count[i][j + 1] != float('inf') and count[i][
                j + 1] + 1 < count[i][j]:
                count[i][j] = count[i][j + 1] + 1
                changed = True
    # print(count)
    # print(changed)
    if not changed:
        return count[-1][-1]
    else:
        # print("1")
        return visited()


print(visited())
