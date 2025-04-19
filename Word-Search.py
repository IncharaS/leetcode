from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ## time com = 0(m*n*4^L), sc = O(l)
        row, col = len(board), len(board[0])
        visited = set()

        # Early pruning
        if len(word) > row * col:
            return False

        board_counts = Counter()
        word_counts = Counter(word)
        for r in board:
            board_counts.update(r)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        def dfs(i, j, index):
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            if (i, j) in visited or board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            visited.add((i, j))
            res = (dfs(i + 1, j, index + 1) or
                   dfs(i - 1, j, index + 1) or
                   dfs(i, j + 1, index + 1) or
                   dfs(i, j - 1, index + 1))
            visited.remove((i, j))
            return res

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
