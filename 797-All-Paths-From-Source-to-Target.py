class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ## adjacency list is not need as the `graph` is given
        result = []
        n = len(graph)
        def dfs(node, path):
            path.append(node)
            if node == n - 1:
                result.append(path[:])
            for i in graph[node]:
                dfs(i, path)
            path.pop()

        dfs(0, [])
        return result