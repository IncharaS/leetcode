# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        \\\
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        \\\
    ## divide and conquer
    ## function should find max, divide array and add node to tree

        ##base case
        if not nums:
            return None
            
        element = max(nums)
        index = nums.index(element)

        node = TreeNode(element)

        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])

        return node
    