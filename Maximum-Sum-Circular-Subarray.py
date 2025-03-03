class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = nums[0]
        global_max = nums[0]

        local_min = nums[0]
        global_min = nums[0]
        total_sum = nums[0]
        ## keep track of minimum subarray in the same for loop
        ## you can later subtract the min subarray from total sum
        ## for this, count the totalsum of the array in the same for loop 
        for i in range(1, len(nums)):

            local_max = max(nums[i], local_max + nums[i])
            if local_max > global_max:
                global_max = local_max
            local_min = min(nums[i], local_min + nums[i])
            if local_min < global_min:
                global_min = local_min
            total_sum += nums[i]
        if total_sum == global_min:
            return global_max

        return max(global_max , total_sum - global_min)
        