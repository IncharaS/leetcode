class Solution(object):
    def permute(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        res = []
        

        def dfs(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
        dfs(nums, [], res)

        return res
