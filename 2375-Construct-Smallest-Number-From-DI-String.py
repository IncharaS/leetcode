class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        ## add elements to stack, pop only if you see an "I", assigning numbers in the reverse order
        ## This way makes sure the "D"s down "I" get the greater number
        stack = []
        result = ''
        num = 1
        ## extra element "I" at last to pop everything
        for i in pattern + "I":
            stack.append(str(num))
            num += 1
            if i == "I":
                while stack: 
                    result += stack.pop()   
        return result

        