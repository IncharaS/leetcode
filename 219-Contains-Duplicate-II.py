class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: bool
        \\\
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict and (i - nums_dict[num] <= k):
                \num still not added to dict, so nums_dict[num] is of already added number\
                return True
            nums_dict[num] = i
        return False
        