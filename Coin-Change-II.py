class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n = len(coins)
        # t = amount
        # dp = [[0 for j in range(t+1)] for i in range(n)]

        # ## base case
        # ## here at last, i.e at a[0] the target can be anything, like (0,6) (0,4) etc, so for all this dp[0][target] fill target/a[0]

        # for i in range(t+1):
        #     if i % coins[0] == 0:
        #         dp[0][i] = 1

        #         ##saying not able to use this coin for calculation
        
        # for i in range(1,n):
        #     for j in range(t+1):
        #         notTake = dp[i-1][j]
        #         take = 0
        #         if j >= coins[i]:
        #             take = dp[i][j-coins[i]]
        #         dp[i][j] = take + notTake
        # print(dp)
        # return dp[n-1][t]
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[amount]
   
