def calculateMinimumHP(dungeon):
    if dungeon == []:
        return 0
    row = len(dungeon)
    col = len(dungeon[0])
    dp = [[0] * col for i in range(row)]
    dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
    for i in range(col - 2, -1, -1):
        dp[-1][i] = max(1, dp[-1][i + 1] - dungeon[-1][i])

    for j in range(row - 2, -1, -1):
        dp[j][-1] = max(1, dp[j + 1][-1] - dungeon[j][-1])

    for j in range(col - 2, -1, -1):
        for i in range(row - 2, -1, -1):
            dp_min = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(1, dp_min - dungeon[i][j])
    return dp
print(calculateMinimumHP([[0,0,0],[1,1,-1]]))