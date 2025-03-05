class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        if not self.head: return
        if index == 0:
            return self.head.val
        else:
            current = self.head
            i = 0
            while(i < index):
                current = current.next
                i += 1
        return current.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        a = ListNode(val)
        a.next = self.head
        self.head = a
        self.length += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        a = ListNode(val)
        ## create a new node with val
        ##check if its the head node

        if not self.head:
            self.head = a
            self.length += 1
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = a
            self.length += 1
        
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.length:
            return
        a = ListNode(val)
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        i = 0
        while(i < index-1):
            current = current.next
            i += 1
        next_index = current.next
        current.next = a
        a.next = next_index
        self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            i = 0
            while(i < index-1):
                current = current.next
                i += 1
            current.next = current.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
