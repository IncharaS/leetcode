# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        \\\
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        dummy = ListNode()
        dummy_var = dummy
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val > cur2.val:
                dummy_var.next = cur2
                cur2 = cur2.next
            else: 
                dummy_var.next = cur1
                cur1 = cur1.next
            dummy_var = dummy_var.next
        if cur1:
            dummy_var.next = cur1
        elif cur2:
            dummy_var.next = cur2
            
        return dummy.next