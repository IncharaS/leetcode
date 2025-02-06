class Solution(object):
    def minSubArrayLen(self, target, nums):
        \\\
        :type target: int
        :type nums: List[int]
        :rtype: int
        \\\
        min_l = 100001
        window_sum = 0
        left = 0
        for i in range(len(nums)):
            window_sum += nums[i]
            while window_sum >= target:
                min_l = min(min_l, i - left + 1)
                window_sum -= nums[left]
                left += 1
        if min_l == 100001: return 0
        return min_l

            
        