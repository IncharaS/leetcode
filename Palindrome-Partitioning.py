class Solution(object):
    def partition(self, s):
        \\\
        :type s: str
        :rtype: List[List[str]]
        \\\
        output = []
        res = []
        n = len(s)
        def is_palindrome(string):
            return string == string[::-1]
        def dfs(index, res):
            if index == n:
                output.append(res[:])
                return
            for i in range(index, n):
                substring = s[index:i+1]
                if is_palindrome(substring):
                    res.append(substring)
                    dfs(i+1, res)
                    res.pop()
                    
        dfs(0, res)
        return output

        