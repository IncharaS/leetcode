import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        minHeap = []
        for i in range(len(heights) - 1):
            if heights[i+1] - heights[i] <= 0:
                continue
            heapq.heappush(minHeap, heights[i+1] - heights[i])
            if len(minHeap) > ladders:
                bricks -= heapq.heappop(minHeap)

                if bricks < 0:
                    return i
        return len(heights) - 1
            