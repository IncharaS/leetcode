class Solution(object):
    def moveZeroes(self, nums):
        \\\
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        \\\
        slow = 0  # Slow points to the position of the next nonzero
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums


        