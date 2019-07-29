def coinChange( coins, amount):
    if coins[0] > amount:
        return 0
    else:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for k in coins:
            if k <= amount:
                dp[k] = 1
        for i in range(1,amount+1):
            tmp = []
            for j in range(len(coins)):
                if i > coins[j] and dp[i - coins[j]] != -1 and  dp[i] != 1:
                    tmp.append(dp[i - coins[j]])
            if tmp != []:
                dp[i] = min(tmp) + 1
            print(dp)
        return dp[amount]
print(coinChange([2],1))