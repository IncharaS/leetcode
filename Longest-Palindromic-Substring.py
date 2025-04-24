class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resL = 0
        if len(s) == 0: return ''
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resL == 0 or resL < r-l+1:
                    print(resL, res)
                    resL = r-l+1
                    res = s[l:r+1]
                    print(resL, res)
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resL == 0 or resL < r-l+1:
                    resL = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1            
        
        return res