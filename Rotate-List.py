class Solution(object):
    def rotateRight(self, head, k):
        \\\
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        \\\
        # Edge case: If the list is empty or there's no rotation needed
        if not head:
            return None
        
        # First, get the length of the list
        cur = head
        length = 1  # Start at 1 because we are counting from the head
        while cur.next:
            cur = cur.next
            length += 1
        
        # Now reduce k if it's greater than length
        k = k % length
        if k == 0:
            return head
        
        # Connect the last node to the head to make it a circular linked list
        cur.next = head
        
        # Move the fast pointer k steps ahead
        fast = head
        for _ in range(length - k - 1):
            fast = fast.next
        
        
        # Now slow is at the new tail, and fast is at the new head
        new_head = fast.next
        fast.next = None  # Break the circular connection
        
        return new_head
