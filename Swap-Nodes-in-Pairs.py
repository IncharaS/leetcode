# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        dummy = ListNode(0)  # Dummy node before head
        dummy.next = head
        pre = dummy  
        while pre.next and pre.next.next:
            ##check if 2 elemnets are left to flip

            a = pre.next
            b = a.next
            ##assign the nodes first

            pre.next = b
            a.next = b.next
            b.next = a
            
            pre = a
        return dummy.next