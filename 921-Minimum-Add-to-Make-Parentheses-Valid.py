class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        ##can't just count because the brackets might be facing the other way
        open_brak, closing_brak = 0, 0
        
        for _ in s:
            if _ == '(':
                open_brak += 1
            else:
                if open_brak > 0:
                    open_brak -= 1
                else: 
                    closing_brak += 1
        return open_brak + closing_brak

        