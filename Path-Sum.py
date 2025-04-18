class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False
        
        def dfs(node, curr_sum):
            if not node or self.found:
                return
            
            curr_sum += node.val
            
            if not node.left and not node.right and curr_sum == targetSum:
                self.found = True
                return
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
        
        dfs(root, 0)
        return self.found
