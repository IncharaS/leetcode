class Solution(object):
    def combinationSum2(self, candidates, target):
        \\\
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        output = []
        res_set = set()
        candidates.sort()
        def dfs(index, res, target):
            if target == 0:
                res_tuple = tuple(res)
                if res_tuple not in res_set:
                    output.append(res)
                    res_set.add(res_tuple)
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicates
                if candidates[i] > target:
                    break
                dfs(i+1, res + [candidates[i]], target - candidates[i])
        dfs(0, [], target)
        return output
        