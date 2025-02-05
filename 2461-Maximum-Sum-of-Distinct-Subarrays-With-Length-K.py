from collections import defaultdict

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict_ = defaultdict(int)  # Track frequency of elements in the current window
        window_sum = 0
        max_sum = 0

        for i in range(k):
            dict_[nums[i]] += 1
            window_sum += nums[i]

        if len(dict_) == k:
            max_sum = window_sum

        for i in range(k, len(nums)):
            left_elem = nums[i - k]
            dict_[left_elem] -= 1
            window_sum -= left_elem
            if dict_[left_elem] == 0:
                del dict_[left_elem]  

            right_elem = nums[i]
            dict_[right_elem] += 1
            window_sum += right_elem

            if len(dict_) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum
