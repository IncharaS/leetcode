class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)

        time = 0
        cooldown = deque()

        while maxheap or cooldown:
            time += 1
            if maxheap:
                current_task = heapq.heappop(maxheap) + 1 ## +1 instead of -1 to decrese
                if current_task != 0: ## its not done yet, push it to cooldown
                    cooldown.append((time + n, current_task))
            
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(maxheap, cooldown.popleft()[1])
        
        return time

