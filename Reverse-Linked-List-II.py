# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        \\\
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        \\\
        if not head or left == right:
            return head
        ## head is None, it returns None

        dummy = ListNode()
        dummy.next = head

        # prev =  head, doesnt work, what if left is at head
        # we want prev at left - 1
        prev = dummy
        for i in range(left-1):
            prev = prev.next

        ## reverse the target list
        ## cur = head, but here, its prev.next
        store_prev = prev
        prev, curr = None, store_prev.next

        for i in range(right - left + 1):
            nexxt = curr.next
            curr.next = prev
            prev = curr
            curr = nexxt
        
        ## before next step, 
        store_prev.next.next = curr

        ## cur is at 5, prev at 4
        ## store_prev is at 1
        store_prev.next = prev

        return dummy.next