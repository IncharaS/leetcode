from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        # Dictionary to store frequency of characters
        dictionary = Counter(s)
        # Stack to build the final result
        stack = []
        # Set to track which characters are in the result
        in_stack = set()

        for i in s:
            # Decrease the frequency of the current character
            dictionary[i] -= 1

            # If the character is already in the result, skip it
            if i in in_stack:
                continue

            # Ensure lexicographical order by removing characters from stack
            # that are greater than the current character and will appear later
            while stack and stack[-1] > i and dictionary[stack[-1]] > 0:
                # Remove the character from stack and in_stack set
                removed = stack.pop()
                in_stack.remove(removed)

            # Add the current character to the stack and in_stack set
            stack.append(i)
            in_stack.add(i)

        # Join the stack into a string and return the result
        return ''.join(stack)
