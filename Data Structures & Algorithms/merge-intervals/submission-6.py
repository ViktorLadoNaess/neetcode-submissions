class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        print(intervals)
        res=[]
        i = 0
        while i <len(intervals):
            l ,r = intervals[i][0], intervals[i][1]
            while i+1 <len(intervals) and r >= intervals[i+1][0]:
                i+=1
                r = max(r,intervals[i][1])
            res.append([min(l,intervals[i][0]),max(r,intervals[i][1])])
            i +=1
        return res
            