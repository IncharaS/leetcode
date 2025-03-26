class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        \\\
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        \\\
        stack = []
        next_greater = {}  # Dictionary to store next greater elements
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[num] for num in nums1]
