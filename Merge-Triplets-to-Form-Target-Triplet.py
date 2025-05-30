class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = False
        
        for trip in triplets:
            if not a and trip[0] == target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                a = True
            if not b and trip[0] <= target[0] and trip[1] == target[1] and trip[2] <= target[2]:
                b = True
            if not c and trip[0] <= target[0] and trip[1] <= target[1] and trip[2] == target[2]:
                c = True
        return a and b and c