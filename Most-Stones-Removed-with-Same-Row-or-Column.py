class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(node):
            if node not in parent:
                parent[node] = node
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for i, j in stones:
            union(i, j + 10001)  # offset column

        # Count unique root nodes
        roots = set(find(x) for x in parent)
        return len(stones) - len(roots)
