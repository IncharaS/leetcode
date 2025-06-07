class Solution:
    def checkValidString(self, s: str) -> bool:

        low = high = 0  # min and max possible open brackets

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1    
                high += 1

            if high < 0:
                return False
            if low < 0:
                low = 0

        return low == 0
        # dp = [[False] * (len(s) + 1) for i in range(len(s) + 1)]
        # dp[0][0] = True
        # # at len 0, open bracket is 0 => True

        # for i in range(len(s)):
        #     for j in range(len(s)+1):
        #         if not dp[i][j]:
        #             continue
        #         if s[i] == '(':
        #             dp[i+1][j+1] = True
        #             ## in the next row, when opencount will be +1
        #         if s[i] == ')':
        #             if j > 0:
        #                 dp[i+1][j-1] = True
        #         if s[i] == '*':
        #             if j > 0:
        #                 dp[i+1][j-1] = True
        #             dp[i+1][j+1] = True
        #             dp[i+1][j] = True
        # # print(dp)
        # return dp[len(s)][0]
                
            