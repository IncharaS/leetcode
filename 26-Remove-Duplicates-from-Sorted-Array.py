class Solution(object):
    def removeDuplicates(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        slow = 0
        n = len(nums)
        for fast in range(1, n):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
        
        