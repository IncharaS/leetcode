from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        INF = 2**31 - 1
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Step 1: Enqueue all gates (value == 0)
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # Step 2: BFS from all gates at once
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and rooms[ni][nj] == INF:
                    rooms[ni][nj] = rooms[i][j] + 1
                    queue.append((ni, nj))
