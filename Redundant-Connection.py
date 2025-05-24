class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find_parent(node):
            if parent[node] != node:
                parent[node] = find_parent(parent[node])
            return parent[node]

        for u, v in edges:
            root_u = find_parent(u)
            root_v = find_parent(v)

            # if same root → cycle
            if root_u == root_v:
                return [u, v]
            else:
                # merge: union one root into another
                parent[root_v] = root_u
