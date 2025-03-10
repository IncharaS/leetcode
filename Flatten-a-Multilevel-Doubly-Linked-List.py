"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return None
        
        def dfs(node):
            if not node:
                return None
                ## when this dfs ends is, 
                ## when it is at the last node it it's level

            cur = node
            prev = None
            while cur:
                if cur.child:
                    ## we want the last node of that child level,
                    ## return that, that is prev

                    last_node_of_child_level = dfs(cur.child)

                    ## join this with the rest of the list, store next_node
                    # Store the next node because we need to come back to it
                    next_node = cur.next

                    # Attach the flattened child list to the current node
                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None

                    # Connect the last node of the child list to the next node
                    if next_node:
                        last_node_of_child_level.next = next_node
                        next_node.prev = last_node_of_child_level

                    # Move `cur` to the next node after the child list
                    cur = last_node_of_child_level

                else:
                    prev = cur
                    cur = cur.next
                    ## while loop ends at cur = none, so maintain prev to return
                        
            return prev
        
        first_node = head
        dfs(first_node)

        return head

        