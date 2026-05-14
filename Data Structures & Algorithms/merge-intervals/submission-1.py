class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res =[]
        for lower,upper in intervals:
            if not res or lower > res[-1][1]:
                res.append([lower,upper])
            else: 
                res[-1][1]=max(res[-1][1], upper)
        return res
