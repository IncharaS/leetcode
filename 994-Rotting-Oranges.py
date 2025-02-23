class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        # visited = [[0] * n for i in range(m)]
        ## Stwp 1: insert Initial rotten orragnes into queue
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_oranges += 1
        
        ## Step 2: BFS
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0
        while queue and fresh_oranges > 0:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()
                for a,b  in directions:
                    ni, nj = i + a, j + b
                    ## if its fresh orange then it goes bad
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_oranges -= 1
                        queue.append((ni, nj))
            count += 1
        if fresh_oranges > 0: return -1             
        return count


        