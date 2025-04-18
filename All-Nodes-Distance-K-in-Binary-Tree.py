class Solution:
    def set_parents(self, node, parent=None):
        if node:
            node.parent = parent
            self.set_parents(node.left, node)
            self.set_parents(node.right, node)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.res = []
        self.visited = set()
        self.set_parents(root)

        def dfs(node, distance):
            if not node or node in self.visited:
                return
            self.visited.add(node)
            if distance == 0:
                self.res.append(node.val)
                return
            dfs(node.left, distance - 1)
            dfs(node.right, distance - 1)
            dfs(getattr(node, 'parent', None), distance - 1)

        dfs(target, k)
        return self.res
