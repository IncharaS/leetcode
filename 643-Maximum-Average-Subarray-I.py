class Solution(object):
    def findMaxAverage(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: float
        \\\
        n = len(nums)
        sum_window = sum(nums[:k])
        max_sum = sum_window
        for i in range(n-k):
            sum_window -= nums[i]
            sum_window += nums[i+k]
            max_sum = max(max_sum, sum_window)
        return max_sum/float(k)
        