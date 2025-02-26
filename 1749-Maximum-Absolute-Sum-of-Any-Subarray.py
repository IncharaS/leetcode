class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Kadanes algorithm (both for positive and negetive)

        local_sum_positive = 0
        global_max_positive = 0
        for i in range(len(nums)):
            local_sum_positive = max(local_sum_positive + nums[i], nums[i])
            global_max_positive = max(global_max_positive, local_sum_positive)

        local_sum_negative = 0
        global_max_negative = 0
        for i in range(len(nums)):
            local_sum_negative = min(local_sum_negative + nums[i], nums[i])
            global_max_negative = min(global_max_negative, local_sum_negative)

        return max(-global_max_negative, global_max_positive)
        