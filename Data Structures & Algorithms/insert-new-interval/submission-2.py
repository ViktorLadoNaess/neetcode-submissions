
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res= []
        new_lower = newInterval[0]
        new_upper = newInterval[1]
        i = 0
        while i < len(intervals) and intervals[i][1] < new_lower:
                res.append(intervals[i])
                i +=1
        while i < len(intervals) and intervals[i][0] <= new_upper:
            new_lower = min(new_lower,intervals[i][0])
            new_upper = max(new_upper,intervals[i][1])
            i+=1
        res.append([new_lower,new_upper])
        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        return res


