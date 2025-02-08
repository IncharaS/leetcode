class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Sliding Window. First think about how to move left. Then right.
        seen = set()
        left = 0
        maxVal = 0
        curSum = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curSum -= nums[left]
                left += 1
            seen.add(nums[right])
            curSum += nums[right]
            maxVal = max(maxVal, curSum)
        return maxVal
