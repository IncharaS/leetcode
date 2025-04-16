# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderHelper(self, result, node):
        ##base case - leaf nodes
        if not node:
            return
        self.postorderHelper(result, node.left)
        self.postorderHelper(result, node.right)
        result.append(node.val)


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorderHelper(result, root)

        return result

        