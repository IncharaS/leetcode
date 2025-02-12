class Solution(object):
    def convert(self, s, numRows):
        \\\
        :type s: str
        :type numRows: int
        :rtype: str
        \\\
        ## edge cases
        if len(s) <= numRows:
            return s
        if numRows == 1: return s
        rows = [\\] * numRows
        index, step = 0, 1
        for character in s:
            rows[index] += character

            if index == 0: ##first row
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return \\.join(rows)
            

        