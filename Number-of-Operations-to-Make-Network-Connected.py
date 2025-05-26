class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [-1] * n
        for i in range(n):
            parent[i] = i
        connections.sort()
        ## find the parent of the node
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        count = 0
        components = n

        for i,j in connections:
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_j] = root_i
                components -= 1
            else:
                ## already i and j belong to the same component
                ## so redundant connection
                count += 1

        if components - 1 > count: return -1
        else: return components - 1