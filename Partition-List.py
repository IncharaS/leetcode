class Solution(object):
    def partition(self, head, x):
        \\\
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        \\\
        # Create two dummy nodes for the two partitions
        small_dummy_list = ListNode()
        s_head = small_dummy_list
        greater_dummy_list = ListNode()
        g_head = greater_dummy_list

        cur = head
        while cur:
            if cur.val < x:
                small_dummy_list.next = cur
                small_dummy_list = small_dummy_list.next  # Move the small list pointer forward
            else:
                greater_dummy_list.next = cur
                greater_dummy_list = greater_dummy_list.next  # Move the greater list pointer forward
            cur = cur.next
        
        # End the greater list
        greater_dummy_list.next = None
        
        # Connect the two partitions
        small_dummy_list.next = g_head.next
        
        return s_head.next  # Return the head of the partitioned list
