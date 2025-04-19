class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        nums_counter = Counter(nums)
        i = 0
        for char, count in sorted(nums_counter.items()):
            for _ in range(count):
                nums[i] = char
                i += 1
