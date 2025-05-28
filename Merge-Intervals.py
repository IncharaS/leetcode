class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        stack = []
        for interval in intervals:
            if stack and interval[0] <= stack[-1][1]: 
                stack[-1][1] = max(stack[-1][1], interval[1])
            else: 
                stack.append(interval)
        return stack