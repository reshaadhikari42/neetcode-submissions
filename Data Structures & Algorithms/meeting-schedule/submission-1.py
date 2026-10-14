"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda x:x.start)
        start, end = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            if end > intervals[i].start:
                return False
            end = intervals[i].end
        return True