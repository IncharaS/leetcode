class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        
        # First pass: identify rows and columns with zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Second pass: zero out identified rows
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
