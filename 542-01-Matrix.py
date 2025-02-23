class Solution(object):
    def updateMatrix(self, mat):
        \\\
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        \\\
        m = len(mat)
        n = len(mat[0])
        output = [[float('inf')] * n for i in range(m)] 
            
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    queue.append((i,j))
        
        directions = [(-1,0), (0, -1), (1, 0), (0, 1)]

        while queue:
            i, j = queue.popleft()
            for (newI, newJ) in directions:
                iNow, jNow = i+newI, j+newJ
                if 0 <= iNow < m and 0 <= jNow < n and output[iNow][jNow] == float('inf'):
                    output[iNow][jNow] = output[i][j] + 1
                    queue.append((iNow, jNow))
        return output