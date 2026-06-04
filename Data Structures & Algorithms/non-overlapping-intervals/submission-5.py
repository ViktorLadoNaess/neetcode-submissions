class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        c =0
        lower=intervals[0][0]
        upper = intervals[0][1]
        for i in intervals[1:]:
            if i[0]< upper:
                c +=1
                if upper > i[1]:
                    upper = i[1]
                    lower= i[0]


            else:
                upper = i[1]
                lower = i[0]
        return c
