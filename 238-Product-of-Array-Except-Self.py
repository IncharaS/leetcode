class Solution(object):
    def productExceptSelf(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[int]
        \\\
        n = len(nums)

        ans = [0] * n

        suffix_product = 1
        for i in range(n):
            ans[i] = suffix_product
            suffix_product *= nums[i]
        
        prefix_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= prefix_product
            prefix_product *= nums[i]
        return ans

        