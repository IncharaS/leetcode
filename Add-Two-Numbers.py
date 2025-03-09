class Solution(object):
    def addTwoNumbers(self, l1, l2):
        \\\
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        carry = 0
        dummy_head = ListNode()  # Dummy node to simplify the result list
        current = dummy_head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            val = total % 10
            current.next = ListNode(val)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy_head.next