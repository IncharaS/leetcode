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
            ## because time is always the current processing time
        return output

        ''' the system time is 0.
        Now scan from first, the first task is available at 1, 
        so you'll update the sytem time to 1.
        And now add all the process which are available at this time 
        into the Heap. (processing time, index)
        Pop ONLY 1 element out of heap (seriel execution)
        if this task taken x processing time, then the current 
        system time is time += x,
        by this time there will be more processes available.
        so add all of them. and repeat until:
        1. len(task) is reached = nothing to add
        2. heap is empty = nothing to pop'''
        