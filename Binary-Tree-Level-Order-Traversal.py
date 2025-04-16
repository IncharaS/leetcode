# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = deque()
        queue.append(root)
        while queue:
            l = len(queue)
            i = 0
            list_nodes = []
            while i < l:   
                node = queue.popleft() 
                list_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            output.append(list_nodes)
        return output