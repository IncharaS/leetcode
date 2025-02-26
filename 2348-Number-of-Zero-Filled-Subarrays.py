class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        zero_streak = 0
        
        for num in nums:
            if num == 0:
                zero_streak += 1
                count += zero_streak  # Every zero extends previous subarrays
            else:
                zero_streak = 0  # Reset on encountering a non-zero
        
        return count


        