import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency_map = Counter(s)
        heap = [(-f, letter) for letter, f in frequency_map.items()]
        heapq.heapify(heap)

        output = []
        prev_f, prev_letter = 0, ""

        while heap:
            curr_f, curr_letter = heapq.heappop(heap)
            output.append(curr_letter)
            if prev_f < 0:
                heapq.heappush(heap, (prev_f, prev_letter))
            prev_f, prev_letter = curr_f + 1, curr_letter 

        return "".join(output) if len(output) == len(s) else ""
