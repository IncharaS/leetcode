# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        preorder = deque(preorder)
        def dfs(start, end):
            if start > end: return
            if not preorder: return
            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]
            root.left = dfs(start, mid-1)
            root.right = dfs(mid+1, end)
            return root
        return dfs(0, len(inorder))
