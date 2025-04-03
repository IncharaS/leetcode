class Solution(object):
    def subsets(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        output = []

        res = []
        n = len(nums)
        def dfs(res, nums):
            if not nums:
                output.append(res)
                return 
            output.append(res)
            for i in range(len(nums)):
                dfs(res + [nums[i]], nums[i+1:])
        dfs(res, nums)
        return output
        