class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        count = 0
        for i in range(len(s)):
            expand(i, i)     # Odd-length
            expand(i, i + 1) # Even-length

        return count
