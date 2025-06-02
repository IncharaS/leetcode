class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, path):
            res.append(path[:])  # Add the current subset
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # Skip duplicates
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res