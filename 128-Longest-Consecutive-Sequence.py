class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        if len(nums) == 0:
            return 0
        set_of_nums = set(nums)
        ## 
        max_length = 0
        length = 0
        for n in set_of_nums:
            if n-1 not in set_of_nums:
                curr = n
                length = 1
                while curr + 1 in set_of_nums:
                    length += 1
                    curr += 1
            max_length = max(length, max_length)
        return max_length

