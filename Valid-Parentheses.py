class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        dictionary = {']':'[', ')':'(', '}':'{'}
        stack = []
        for i in s:
            if i in dictionary:
                if stack: 
                    last_element_in_stack = stack.pop()
                    if last_element_in_stack != dictionary[i]:
                        return False
                else: stack.append(i)
            else:
                stack.append(i)
        if stack: return False
        return True



        #     elif i == ')':
        #         if stack:
        #             last_element_in_stack = stack.pop()
        #             if last_element_in_stack != '(':
        #                 return False
        #         else: stack.append(i)
        #     elif i == '}':
        #         if stack:
        #             last_element_in_stack = stack.pop()
        #             if last_element_in_stack != '{':
        #                 return False
        #         else: stack.append(i)
        #     else:
        #         stack.append(i)
        # if stack: return False
        # return True