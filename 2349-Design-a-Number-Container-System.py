import collections

class NumberContainers(object):

    def __init__(self):
        self.map = {} 
        self.numbers = collections.defaultdict(SortedSet)  
    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.map:
            old_number = self.map[index]
            if old_number in self.numbers:
                self.numbers[old_number].discard(index)
                if not self.numbers[old_number]:
                    del self.numbers[old_number]  
        self.map[index] = number
        self.numbers[number].add(index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number in self.numbers and self.numbers[number]:
            return self.numbers[number][0] 
        return -1
