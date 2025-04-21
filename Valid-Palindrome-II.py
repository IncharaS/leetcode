class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s_):
            return s_ == s_[::-1]
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                bool = is_palindrome(s[i+1:j+1]) or is_palindrome(s[i:j])
                return bool
            i += 1
            j -= 1
        return True