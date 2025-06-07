class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        
        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor ^= i
        
        # XOR all numbers in nums
        for num in nums:
            xor ^= num
        
        return xor