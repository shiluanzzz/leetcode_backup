def solve2017(grid):


    dp={}
    path=[]
    def dfs(x,y,reward):
        dp.setdefault("{}-{}".format(x,y),-1)
        if  dp["{}-{}".format(x,y)]!=-1:
            return dp["{}-{}".format(x,y)]
        if x>1 or y>len(grid[0])-1:
            return -1
        if x==1 and y==len(grid[0])-1:
            return reward+grid[x][y]

        case1 = dfs(x+1,y,reward+grid[x][y])
        case2 = dfs(x,y+1,reward+grid[x][y])
        if case1>case2:
            path.append([x+1,y])
            dp["{}-{}".format(x, y)] = reward + grid[x+1][y]
            return reward+case1
        else:
            path.append([x,y+1])
            dp["{}-{}".format(x, y)] = reward + grid[x][y+1]
            return reward+case2
    dfs(0,0,0)
    print(path)
    print(dp)
if __name__ == '__main__':
    solve2017([
        [0,1,1,1,1,1,99],
        [2,2,2,2,2,2,2]
    ])
