class Solution(object):
    def dailyTemperatures(self, temperatures):
        \\\
        :type temperatures: List[int]
        :rtype: List[int]
        \\\

        stack = []
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                a = stack.pop()
                res[a] = index - a
            stack.append(index)
        return res
        