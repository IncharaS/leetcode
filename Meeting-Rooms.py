class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i: i[1])
        length = len(intervals)
        if length == 0 or length == 1:
            return True
        previous_interval_end = intervals[0][1]
        for interval in range(1, length):
            if intervals[interval][0] < previous_interval_end:
                return False
            previous_interval_end = intervals[interval][1]
        return True