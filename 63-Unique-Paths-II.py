class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        col_true = True
        row_true = True
        dp = [[0] * n for i in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]
        
        