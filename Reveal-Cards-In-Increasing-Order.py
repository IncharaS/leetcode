class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        ## queue of indices
        ## result array with 0's
        deck.sort()
        queue = deque(range(len(deck)))
        result = [0] * len(deck)
        skip = False
        for n in deck:
            index = queue.popleft()
            if skip:
                queue.append(index)
                skip = False
                index = queue.popleft()
            result[index] = n
            skip = True
            # print(queue, result)
        return result