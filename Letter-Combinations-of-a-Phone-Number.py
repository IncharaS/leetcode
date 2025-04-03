class Solution(object):
    def letterCombinations(self, digits):
        \\\
        :type digits: str
        :rtype: List[str]
        \\\
        dic = { \2\: \abc\, \3\: \def\, \4\:\ghi\, \5\:\jkl\, \6\:\mno\, \7\:\pqrs\, \8\:\tuv\, \9\:\wxyz\}
        if len(digits) == 0:
            return []
        output = []
        n = len(digits)
        def dfs(index, res):
            if len(res) == n:
                output.append(res)
                return
            for i in range(index, n):
                letter_string = dic[digits[i]] 
                for j in letter_string:
                    dfs(i+1, res + j)
                
        dfs(0, '')
        return output