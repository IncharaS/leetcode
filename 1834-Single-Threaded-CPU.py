import heapq

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """

        indexed_tasks = sorted((tasks[i][0], tasks[i][1], i) for i in range(len(tasks)))

        output = []
        min_heap = []  
        time, i, n = 0, 0, len(indexed_tasks)
        while i < n or min_heap:
            if not min_heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]
            while i < n and indexed_tasks[i][0] <= time:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))  # (processing_time, index)
                i += 1 
            processing_time, index = heapq.heappop(min_heap)
            output.append(index)
            time += processing_time  
        return output
