# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxV):
            nonlocal count
            if not node:
                return
            if node.val >= maxV:
                count += 1
                maxV = node.val
            if node.left:
                dfs(node.left, maxV)
            if node.right:
                dfs(node.right, maxV)

        count = 0
        dfs(root, root.val)
        return count