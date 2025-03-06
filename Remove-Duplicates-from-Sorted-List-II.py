# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head
        slow = dummy
        fast = head

        while fast:
            flag = False  # Track if duplicates exist

            # Detect duplicates
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
                flag = True

            # If duplicates were found, skip them
            if flag:
                slow.next = fast.next
            else:
                slow = slow.next  # Move slow forward only if no duplicates

            fast = fast.next  # Move fast forward

        return dummy.next  # Return new head

