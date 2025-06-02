class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp since you make a decision to choose a character from s1 or s2
        # dp of size len(s1) + 1, len(s2) + 1
        # dp[0][0] == 0 because you can make empty string with either
        # fill first row and column if the corresponding letters match with s3 at the same indices
        # fill the rest of the table if s3(i+j-1) matches either and s1(i) or s2(j) and the previous cell is true
        # this means that if s3(i+j-1) matches then there exists a situation that rest of the string is present in either s1 or s2

        l = len(s1) + 1
        m = len(s2) + 1
        dp = [[False] * m for i in range(l)]
        dp[0][0] = True
        if len(s3) != (l+m - 2) : return False
        for i in range(1, l):
            dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]
        
        for i in range(1, m):
            dp[0][i] = s2[i-1] == s3[i-1] and dp[0][i-1]
        
        for i in range(1, l):
            for j in range(1, m):
                dp[i][j] = (s3[i+j-1] == s1[i-1] and dp[i-1][j]) or \\
                            (s3[i+j-1] == s2[j-1] and dp[i][j-1])
        return dp[l-1][m-1]
         