class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        
        for source, target ,time in times:
            adj_list[source].append((time, target))
        visited=set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node) 
            if len(visited) == n:
                return travel_time
            for time, adjacent_node in adj_list[node]:
                if adjacent_node not in visited:
                    heapq.heappush(heap, (travel_time + time, adjacent_node))
        return -1
        ## bfs
        # graph = defaultdict(list)
        # for time in times:
        #     graph[time[0]].append((time[1], time[2]))
        
        # queue = deque()
        # visited = set()
        # queue.append(k)
        # total_time = 0

        # while queue:
        #     node = queue.popleft()
        #     visited.add(node)
        #     time_in_level = 0
        #     for target_node, time in graph[node]:
        #         if target_node not in visited:
        #             time_in_level = max(time_in_level, time)
        #             queue.append(target_node)
        #     total_time += time_in_level
        # return total_time if total_time != 0 else -1