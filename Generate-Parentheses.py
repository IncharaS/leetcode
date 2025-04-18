class Solution(object):
    def generateParenthesis(self, n):
        \\\
        :type n: int
        :rtype: List[str]
        \\\
        def dfs(l,r,s):
            # if len(s) == n * 2:
            if l == r == n:
                res.append(s)
                return
            
            if l<n:
                dfs(l+1, r, s + '(')
            if r < n and l > r:
                dfs(l, r+1, s+')')
        res = []
        dfs(0, 0, '')  
        return res      