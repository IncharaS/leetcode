class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #no loops, no repeated edges
        
        # if len(edges) != n - 1: return False
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
        count = 0
        for i in edges:
            parent1 = find_parent(i[0])
            parent2 = find_parent(i[1])
            if parent1 == parent2:
                continue
            else:
                parent[parent2] = parent1
                count += 1
        print(parent)

        return n - count
   