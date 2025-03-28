# class Solution(object):
#     def find132pattern(self, nums):
#         \\\
#         :type nums: List[int]
#         :rtype: bool
#         \\\
#         if len(nums) < 3:
#             return False

#         stack = []  # Monotonic decreasing stack (stores pairs of (nums[j], minI))
#         minI = nums[0]  # Tracks the smallest value before nums[j]

#         for i in range(1, len(nums)):
#             # Debugging output
            
#             # Check if nums[i] (potential nums[k]) forms a 132 pattern
#             while stack and nums[i] >= stack[-1][0]:  # If nums[i] > stack[-1] (potential nums[j])
#                 stack.pop()  # Update minI with previous min

#             if stack and nums[i] > stack[-1][1]:  # Found a valid 132 pattern
#                 return True

#             # Push (nums[i], minI) onto the stack
#             stack.append((nums[i], minI))
#             minI = min(minI, nums[i])

#         return False
class Solution(object):
    def find132pattern(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\
        stack = []  # Monotonic decreasing stack for nums[k]
        second_max = float('-inf')  # This stores nums[k]

        # Traverse from right to left
        for num in reversed(nums):
            # If num < second_max (nums[i] < nums[k]), pattern found
            if num < second_max:
                return True
            
            # Maintain decreasing order in stack
            while stack and stack[-1] < num:
                second_max = stack.pop()  # Pop and update second_max (potential nums[k])
                print(stack)
            stack.append(num)  # Push current number (potential nums[j])
        return False