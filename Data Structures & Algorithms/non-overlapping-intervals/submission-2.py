class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        curr_end = intervals[0][1]
        for lower, upper in intervals[1:]:
            if lower < curr_end:
                count +=1
                curr_end = min(upper, curr_end)
            else:
                curr_end = upper
        return count
