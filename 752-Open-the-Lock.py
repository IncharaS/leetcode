class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        ## to find shortest path in unweighted grapg, this is a BFS problem
        ## a graph problem
        ## queue = nodes, with +1 and -1 increments to next state
        ## pop the queue and if its target return
        ## visited nodes( to avoid redundancy) also add deadends to this because 

        queue = deque()
        if "0000" in deadends: return -1
        queue.append('0000')
        count = 0
        visited = set(deadends)
        visited.add('0000')
        while queue:
            length = len(queue)
            for _ in range(length):
                num = queue.popleft()
                if num == target:
                    return count
                for i in range(4):
                    for delta in (-1, 1):
                        new_i = (int(num[i]) + delta) % 10
                        new_num = num[:i] + str(new_i) + num[i+1:]

                        if new_num in visited:
                            continue
                        else: 
                            queue.append(new_num)
                            visited.add(new_num)
            count += 1
        return -1