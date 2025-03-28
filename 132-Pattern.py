class Solution(object):
    def find132pattern(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\
        if len(nums) < 3:
            return False

        stack = []  # Monotonic decreasing stack (stores pairs of (nums[j], minI))
        minI = nums[0]  # Tracks the smallest value before nums[j]

        for i in range(1, len(nums)):
            # Debugging output
            
            # Check if nums[i] (potential nums[k]) forms a 132 pattern
            while stack and nums[i] >= stack[-1][0]:  # If nums[i] > stack[-1] (potential nums[j])
                stack.pop()  # Update minI with previous min

            if stack and nums[i] > stack[-1][1]:  # Found a valid 132 pattern
                return True

            # Push (nums[i], minI) onto the stack
            stack.append((nums[i], minI))
            minI = min(minI, nums[i])

        return False
