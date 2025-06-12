class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = 1
        maximum = max(piles)

        while minimum < maximum:
            mid = (minimum + maximum ) // 2
            time_taken = 0
            for i in piles:
                time_taken += math.ceil(i / mid)
            if time_taken <= h:
                maximum = mid
            else:
                minimum = mid+1
        return maximum