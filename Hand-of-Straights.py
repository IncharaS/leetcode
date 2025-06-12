class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            currentNumber = minHeap[0]

            for i in range(currentNumber, currentNumber + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True