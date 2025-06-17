class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        length = len(sorted_intervals)
        if length == 0 or length == 1:
            return True
        previous_interval_end = sorted_intervals[0][1]
        for interval in range(1, length):
            if sorted_intervals[interval][0] < previous_interval_end:
                return False
            previous_interval_end = sorted_intervals[interval][1]
        return True