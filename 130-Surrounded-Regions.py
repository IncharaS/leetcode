class Solution(object):
    def solve(self, board):
        \\\
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        \\\

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m  or j >= n  or board[i][j] != \O\:
                return

            board[i][j] = \S\
            dfs(i-1,j)
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i+1, j)


        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if ( i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == \O\:
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == \O\:
                    board[i][j] = \X\
                elif board[i][j] == \S\:
                    board[i][j] = \O\
        