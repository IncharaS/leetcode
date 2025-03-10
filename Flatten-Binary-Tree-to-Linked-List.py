# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        \\\
        if not root:
            return None
        
        def dfs(node):
            if not node:
                return None

            cur = node
            
            left_tail = dfs(cur.left)
            right_tail = dfs(cur.right)

            if left_tail:
                left_tail.right = node.right 
                node.right = node.left
                node.left = None

            return right_tail if right_tail else left_tail if left_tail else node

        dfs(root)

            
        