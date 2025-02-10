class Solution(object):
    def twoSum(self, numbers, target):
        \\\
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        \\\
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]  # Convert to 1-based index
            elif total < target:
                l += 1
            else:
                r -= 1
        return []

        