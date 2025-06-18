class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def dfs(i, j, step ):
            # if (i,j) in visited:
            #     return 
            # visited.add((i, j))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for a, b in directions:
                new_i = i + a
                new_j = j + b
                if 0 <= new_i < len(rooms) and 0 <= new_j < len(rooms[0]):
                    if rooms[new_i][new_j] != -1 and rooms[new_i][new_j] > step + 1:
                        rooms[new_i][new_j] = step + 1
                        dfs(new_i, new_j, step + 1)

        # visited = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
        return rooms