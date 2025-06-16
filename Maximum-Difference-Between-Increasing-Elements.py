class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimum = float('inf')
        maximum_diff = -1
        # print(maximum_diff)
        for i in nums:
            if i <= minimum:
                minimum = i
            else:
                maximum_diff = max(maximum_diff, (i - minimum))
            
        # print(maximum_diff)
        return maximum_diff 