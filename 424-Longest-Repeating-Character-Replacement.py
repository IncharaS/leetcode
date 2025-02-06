class Solution(object):
    def characterReplacement(self, s, k):
        \\\
        :type s: str
        :type k: int
        :rtype: int
        \\\
        left = 0
        count = defaultdict(int)
        max_freq = 0
        max_l = 0
        for right in range(len(s)):
            ## 1. Increase the ftequency of the character in dict
            count[s[right]] += 1
            ## 2. Check if it has the maximum freq
            max_freq = max(max_freq, count[s[right]])
            ## 3. Check how many diff letters are in that window, if more than k, then reduce the window from left

            while ((right - left + 1) - max_freq > k):
                count[s[left]] -= 1
                left += 1

            ## 4. now theres a window where the above condition is true, i.e == k
            max_l = max(max_l, right - left + 1)

        return max_l


        