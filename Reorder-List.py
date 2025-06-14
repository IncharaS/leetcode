# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\
        ##find middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        ## reverse the second half
        second = slow.next
        slow.next = None

        node = None

        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp
        
        first = head
        second = node

        while second:
            temp1 = first.next
            first.next = second
            temp2 = second.next
            second.next = temp1
            first = temp1
            second = temp2


        

        
