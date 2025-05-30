class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in points:
            [a,b] = i
            res.append([math.sqrt(a**2 + b**2), a, b])

        heapq.heapify(res)

        output = []

        for i in range(k):
            ans = heapq.heappop(res)
            output.append([ans[1], ans[2]])
        return output