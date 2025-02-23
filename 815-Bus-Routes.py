class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target: return 0
        map_bus_stops = defaultdict(list)
        for i in range(len(routes)):
            for stops in routes[i]:
                map_bus_stops[stops].append(i)
        bus_queue = deque(map_bus_stops[source])
        count = 1
        visited_stations = set([source])
        visited_buses = set(bus_queue)
        while bus_queue:
            length = len(bus_queue)
            for _ in range(length):
                current_bus = bus_queue.popleft()
                for i in routes[current_bus]:
                    if i == target:  
                        return count
                    if i not in visited_stations:
                        visited_stations.add(i)
                        for next_bus in map_bus_stops[i]:
                            if next_bus not in visited_buses:
                                bus_queue.append(next_bus)
                                visited_buses.add(next_bus)
            count += 1
        return -1