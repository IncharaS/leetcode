class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        parent = {}
        for i in range(n):
            parent[i] = i
        #dictionary[child] = parent

        # find
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]     

        #union
        for i in edges:
            parent1 = find_parent(i[0])
            parent2 = find_parent(i[1])
            if parent1 == parent2:
                return False
            parent[parent2] = parent1
        print(parent)
        return True
