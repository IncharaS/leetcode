class Solution(object):
    def numIslands(self, grid):
        \\\
        :type grid: List[List[str]]
        :rtype: int
        \\\
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == \0\ or visited[i][j]:
                return
            visited[i][j] = 1  # Mark as visited
            # Explore all 4 possible directions
            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i, j + 1)  # Right

        for i in range(m):
            for j in range(n):
                if grid[i][j] == \1\ and not visited[i][j]:
                    count += 1  # Found a new island
                    dfs(i, j)  # Explore the entire island

        return count
