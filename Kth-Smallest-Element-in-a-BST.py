# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(node):
            if not node or self.result: return 
            dfs(node.left)
            self.c += 1
            if k == self.c: 
                # return node.val this just returns to one of dfs func call
                self.result = node.val
            dfs(node.right)
            
        self.c = 0
        self.result = None
        dfs(root)
        return self.result
        # return array[k-1]