# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        \\\
        :type head1, head1: ListNode
        :rtype: ListNode
        \\\
        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:

            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA

        
        