# class Solution:
#     def canPartition(self, nums):
#         total = sum(nums)
#         if total % 2 != 0:
#             return False

#         target = total // 2
#         n = len(nums)

#         dp = [[False] * (target + 1) for _ in range(n + 1)]
        
#         # Base case: sum 0 is always possible (empty subset)
#         for i in range(n + 1):
#             dp[i][0] = True

#         for i in range(1, n + 1):
#             for j in range(1, target + 1):
#                 if j < nums[i - 1]:
#                     dp[i][j] = dp[i - 1][j]  # can't include the number
#                 else:
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

#         return dp[n][target]
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # sum 0 is always possible

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
