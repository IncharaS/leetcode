class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        l = len(s)
        while i < l:
            while i < l and s[i] == '*':
                stack.pop()
                i += 1
            if i < l and s[i] != '*':
                stack.append(s[i])
                i += 1
        return ''.join(stack)
                


        