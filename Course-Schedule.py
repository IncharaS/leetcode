class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for i in prerequisites:
            [a, b] = i
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0

        while queue:
            node = queue.popleft()
            count += 1
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return count == numCourses
