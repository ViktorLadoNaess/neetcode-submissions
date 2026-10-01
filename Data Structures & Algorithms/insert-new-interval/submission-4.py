class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = newInterval[0]
        r = newInterval[1]
        i =0
        res =[]


        while i < len(intervals) and intervals[i][1] < l:
            res.append(intervals[i])
            
            i+=1
        
        while i< len(intervals) and r >= intervals[i][0]:
            l = min(l, intervals[i][0])
            r= max(r, intervals[i][1])
            
            i +=1
        res.append([l,r])
   
        while i <len(intervals):
            res.append(intervals[i])
            i+=1
        return res

        