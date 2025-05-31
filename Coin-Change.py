class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         t = amount
#         dp = [[0 for i in range(t+1)] for j in range(n)]

#         ## base case
#         ## here at last, i.e at a[0] the target can be anything, like (0,6) (0,4) etc, so for all this dp[0][target] fill target/a[0]

#         for i in range(1,t+1):
#             if i % coins[0] == 0:
#                 dp[0][i] = i // coins[0]
#             else:
#                 dp[0][i] = int(1e9)
#                 ##saying not able to use this coin for calculation
        
#         for i in range(1,n):
#             for j in range(t+1):
#                 notTake = dp[i-1][j]
#                 take = int(1e9)
#                 if j >= coins[i]:
#                     take = 1 + dp[i][j-coins[i]]
#                 dp[i][j] = min(take, notTake)
#         ans = dp[n-1][t]
#         if ans >= int(1e9):
#             return -1
#         return ans
        dp = [float(inf)] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        # print(dp)
        return -1 if dp[amount] == float('inf') else dp[amount]