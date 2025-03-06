\\\
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution(object):
    def copyRandomList(self, head):
        \\\
        :type head: Node
        :rtype: Node
        \\\
        if not head:
            return None

        # using interleaving
        # add the fake nodes after original nodes, later add the next and random pointers

        temp = head

        ## interleaving nodes
        while temp:
            new_node = Node(temp.val, next= temp.next)
            temp.next = new_node
            temp = temp.next.next

        ## adding random pointers as well
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            
            temp = temp.next.next



        # Separating the lists
        temp = head
        new_head = head.next  # This will be the head of the copied list
        while temp:
            copy = temp.next
            temp.next = temp.next.next #restoring original list
            if copy.next:
                copy.next = copy.next.next

            temp = temp.next #since its already updated            

        return new_head

        # Time Complexity is O(N), sape complexity O(N)
        # node_map = {}
        # temp = head

        # ## add all the nodes to map, and create corresponding fake nodes

        # while temp:
        #     node_map[temp] = Node(temp.val)
        #     temp = temp.next

        # temp = head

        # ## map next and random
        # while temp:
        #     ##fake.next = original.next
        #     node_map[temp].next = node_map.get(temp.next)
        #     node_map[temp].random = node_map.get(temp.random)
        #     temp = temp.next
            
        # return node_map[head]