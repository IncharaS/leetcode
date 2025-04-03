class Solution(object):
    def combinationSum(self, candidates, target):
        \\\
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        output = []
        def dfs(index, path, target):
            if target == 0:
                output.append(path[:])
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, target - candidates[i])
                path.pop()
        dfs(0, [], target)
        return output