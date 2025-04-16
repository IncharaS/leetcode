# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return 0
        output = []
        queue = deque()
        queue.append(root)
        while(queue):
            l = len(queue)
            sum = 0
            i = 0
            while i < l:
                node = queue.popleft()
                sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                i += 1
            output.append(sum/l)
        return output