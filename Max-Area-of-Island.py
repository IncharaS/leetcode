class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            c = 1
            directions = [(-1,0), (0, -1), (1, 0), (0, 1)]
            stack = [(i,j)]
            visited.add((i,j))
            while stack:
                i,j = stack.pop() #LIFO
                for a,b in directions:
                    ni = i+a
                    nj = j+b
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == 1 and (ni, nj) not in visited:
                            c += 1
                            stack.append((ni,nj))
                            visited.add((ni,nj))
            return c
            

        visited = set()
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    count = dfs(i,j)
                    max_count = max(count, max_count)
        return max_count