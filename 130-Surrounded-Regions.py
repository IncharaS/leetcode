class Solution:
    def solve(self, board: List[List[str]]) -> None:
        \\\
        Do not return anything, modify board in-place instead.
        \\\
        def dfs(a, b):
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                l, r = i + a, j + b
                if l < m and l > -1 and r < n and r > -1 and board[l][r] == 'O' and visited[l][r] == 0:
                    visited[l][r] = 1
                    dfs(l, r)
        def diff_dfs(a, b):
            if a < m-1 and a > 0 and b < n-1 and b > 0 and board[a][b] == 'O' and visited[a][b] == 0:
                visited[a][b] = 1
                board[a][b] = 'X'
                for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    l, r = i + a, j + b
                    diff_dfs(l, r)                                    
        queue = []
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    visited[i][j] = 1
        for i in range(n): ##first row
            if board[0][i] == 'O':
                dfs(0, i)
        for i in range(n): ##last row
            if board[m-1][i] == 'O':
                dfs(m-1, i)
        for i in range(m): ##first column
            if board[i][0] == 'O':
                dfs(i, 0)
        for i in range(m): ##last column
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        for i in range(1, m-1):
            for j in range(1, n-1):
                diff_dfs(i, j)