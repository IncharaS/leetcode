class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        queue = deque()

        for i in range(len(tickets)):
            flag = 0
            if i == k: flag = 1
            queue.append((tickets[i], flag))
        
        count = 0
        while True:
            popped_element, flag = queue.popleft()
            if flag == 1 and popped_element == 1:
                return count + 1
            count += 1
            if popped_element - 1 > 0:
                queue.append((popped_element - 1, flag))        
        return count
