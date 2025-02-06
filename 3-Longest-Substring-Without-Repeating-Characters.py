from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        dict_ = defaultdict(int)
        left = 0  # Left pointer of the sliding window
        max_length = 0

        for right in range(len(s)):
            if s[right] in dict_:
                # Move left pointer to the right of the last seen duplicate character
                left = max(left, dict_[s[right]] + 1)

            dict_[s[right]] = right  # Update last seen index of character
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length
