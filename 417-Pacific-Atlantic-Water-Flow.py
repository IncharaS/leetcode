class Solution(object):
    def pacificAtlantic(self, heights):
        \\\
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        \\\
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(i, j, visited, prev_height):
            if (
                i < 0 or i >= m or j < 0 or j >= n or 
                (i, j) in visited or heights[i][j] < prev_height
            ):
                return
            
            visited.add((i, j))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + dx, j + dy, visited, heights[i][j])
        
        # Start DFS from Pacific Ocean edges (Top row & Left column)
        for i in range(m):
            dfs(i, 0, pacific_reachable, heights[i][0])  # Left column
        for j in range(n):
            dfs(0, j, pacific_reachable, heights[0][j])  # Top row
        
        # Start DFS from Atlantic Ocean edges (Bottom row & Right column)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable, heights[i][n - 1])  # Right column
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable, heights[m - 1][j])  # Bottom row
        
        # Intersection of both reachable sets gives the final result
        return list(pacific_reachable & atlantic_reachable)
