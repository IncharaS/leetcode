class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        dict_ = defaultdict(list)
        for emp in range(n):
            if manager[emp] != -1:
                dict_[manager[emp]].append(emp)
        
        def dfs(emp_id):
            max_time = 0
            ##stopping condition
            if emp_id not in dict_: ## leaf node
                return 0
            for i in dict_[emp_id]:
                max_time = max( max_time, dfs(i))
            return max_time + informTime[emp_id]
            


        return dfs(headID)
        