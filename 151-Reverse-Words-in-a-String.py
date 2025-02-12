class Solution(object):
    def reverseWords(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        words = s.split()  # Automatically removes extra spaces
        return \ \.join(words[::-1])
            
        