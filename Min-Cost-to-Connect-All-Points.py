class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ## prims algo. using heap
        heap = [(0, 0)] ## (cost, index)
        heapq.heapify(heap)
        visited = set()
        res = 0
        while heap:
            cost, index = heapq.heappop(heap)
            if index in visited:
                continue
            visited.add(index)
            res += cost
            for i in range(len(points)):
                if i not in visited: ## node at index i is not visited yet
                    distance = abs(points[index][0] - points[i][0]) + abs(points[index][1] - points[i][1]) 
                    heapq.heappush(heap, (distance, i))
        return res