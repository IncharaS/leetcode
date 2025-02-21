# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        ## to make a dict of nodes, pass root node
        def getParent(node, parent):
            if node is None:
                return
            parentMap[node] = parent

            getParent(node.left, node)
            getParent(node.right, node)
        
        ## to count till k, so pass the target node
        def getNodes(node, level_count):

            ## Step 3: Stoping condition: level_count >= k 
            ## or node is Node 
            ## or node is already visited
            if not node or node in visited or level_count > k:
                return
            
            visited.add(node)
            if level_count == k:
                res.append(node.val)
                return

            ## Step: 1 propogate in 3 directions (left, right, parent)
            getNodes(node.left, level_count+1)
            getNodes(node.right, level_count+1)
            getNodes(parentMap[node], level_count+1)

            ## Step 2: Incresing level_count by 1
            level_count += 1

        parentMap = {}
        getParent(root, None)
        res = []  
        visited = set()
        getNodes(target, 0)

        return res