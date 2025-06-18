class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        def bfs(i, j):
            # if (i,j) in visited:
            #     return 
            # visited.add((i, j))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            queue = deque([(i, j)])
            step = 1
            while queue:
                length = len(queue)
                for _ in range(length):
                    (i_, j_) = queue.popleft()
                    for [a, b] in directions: 
                        new_i = i_ + a
                        new_j = j_ + b
                        if 0 <= new_i < len(rooms) and 0 <= new_j < len(rooms[0]):
                            # visited.add((new_i, new_j))
                            if rooms[new_i][new_j] != -1 and rooms[new_i][new_j] != 0 and rooms[new_i][new_j] > step:
                                rooms[new_i][new_j] = step
                                queue.append((new_i, new_j))
                step += 1

        # visited = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    bfs(i, j)
        return rooms