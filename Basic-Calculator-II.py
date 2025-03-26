class Solution(object):
    def calculate(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        ## O(N) Time complexity
        ## O(1) Space complexity
        op = '+'
        i = 0
        res, prev = 0, 0
        ## 3 cases: curr_char is digit/space/operator
        while i < len(s):
            curr_char = s[i]
            num = 0
            if curr_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1

                ## once you get number, deal with operator present before it
                ## initially its +
                if op == '+':
                    res += num
                    prev = num
                elif op == '-':
                    res -= num
                    prev = -num
                elif op == '*':
                    ## remove prev from result
                    ## example, in 3+2*2, now 5*2, where prev = 2, res = 5
                    ## remove 2 from res, and * with 2. and add it back
                    res -= prev
                    res += prev * num

                    prev = prev * num
                else:
                    res -= prev
                    res += int(float(prev) / num)

                    prev = int(float(prev) / num)
            elif curr_char != ' ':
                op = curr_char
            print(res, \res\)
            i += 1
        return res