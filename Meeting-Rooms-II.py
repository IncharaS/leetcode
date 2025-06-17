class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        ## sort by meeting start time
        heap = [intervals[0][1]]
        count = 1
        heapq.heapify(heap)
        length = len(intervals)

        for i in range(1, length):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            else:
                count += 1
            heapq.heappush(heap, intervals[i][1])
            

        
        return count