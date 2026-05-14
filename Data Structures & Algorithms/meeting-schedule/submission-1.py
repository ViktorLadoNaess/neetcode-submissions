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
        intervals.sort(key=lambda x: x.start)
        
        curr_end = intervals[0].end

        for interval in intervals[1:]:
            if curr_end > interval.start:
                return False
            curr_end = interval.end

        return True
