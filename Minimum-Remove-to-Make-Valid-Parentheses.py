class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ## if (, then push position to stack, pop one verytime u see ).if cant find matching ), then remove that
        ## if ), pop from ( stack, if empty remove this )
        res = list(s)
        i = 0
        j = 0
        l = len(s)
        stack = []
        while i<l:
            if res[j] == ')':
                if stack:
                    stack.pop()
                    j += 1
                else:
                    del res[j]
            elif res[j] == '(':
                stack.append(j)
                j += 1
            else: j += 1
            i += 1
        
        while stack:
            k = stack.pop()
            del res[k]
        return ''.join(res)