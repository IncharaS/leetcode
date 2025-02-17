class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        ##dfs
        record = [0] * 26
        for tile in tiles:
            record[ord(tile) - ord('A')] += 1
        def dfs(record):
            s = 0
            for i in range(26):
                if not record[i]:
                    continue
                record[i] -= 1
                s += dfs(record) + 1
                record[i] += 1 ## add the letter back again, since for loop goes on
            return s
        return dfs(record)


        
        