from collections import deque
\\\
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    \t#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
\\\

class Solution(object):
    def getImportance(self, employees, id):
        \\\
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        \\\
        ## dfs: because I can use queue
        ## Emploess is not a list of lists
        ## ITS A list of Objects, employees[0].id will work
        queue = deque([id])
        importance = 0

        ## employees is not sequential incresing list, so to find 
        ## objects with ID, create a dict (id -> whole object)

        emp_dict = { emp.id: emp for emp in employees}
        while queue:
            print(queue)
            for _ in range(len(queue)):
                node = queue.popleft()                
                queue.extend(emp_dict[node].subordinates)
                importance += emp_dict[node].importance
        return importance      