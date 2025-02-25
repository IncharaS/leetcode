from collections import defaultdict

class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        even_count = 1  # There's always an initial even sum (prefix sum of 0)
        odd_count = 0  
        count = 0
        prefix_sum = 0

        for num in arr:
            prefix_sum += num  # Update running sum

            if prefix_sum % 2 == 0:
                count += odd_count  # Odd sum pairs create valid subarrays
                even_count += 1  # Current prefix sum is even
            else:
                count += even_count  # Even sum pairs create valid subarrays
                odd_count += 1  # Current prefix sum is odd
            
        return count % (10**9 + 7)  # Modulo for large results
