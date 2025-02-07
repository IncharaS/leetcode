from collections import defaultdict

class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product_count = defaultdict(int)
        n = len(nums)
        count = 0
        
        # Count the number of times each product appears
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1  # Store count instead of storing pairs
        
        # Calculate valid quadruples
        for freq in product_count.values():
            if freq > 1:
                count += (freq * (freq - 1) // 2) * 8  # Compute tuple arrangements

        return count
