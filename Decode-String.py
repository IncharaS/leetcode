class Solution(object):
    def decodeString(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        num = 0
        stack = []
        cur_str = \\
        for i in s:
            if i.isdigit():
                num = (num * 10) + int(i)
            elif i == '[':
                stack.append((num, cur_str))
                cur_str = \\
                num = 0
            elif i == ']':
                nums, prev_str = stack.pop()
                cur_str = prev_str + (cur_str * nums)
            else: cur_str += i
        return cur_str
