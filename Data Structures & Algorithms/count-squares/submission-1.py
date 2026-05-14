from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] +=1
        

    def count(self, point: List[int]) -> int:
        res=0
        for p in self.points:
            if (abs(p[0]-point[0]) == abs(p[1]-point[1]) 
                and p[0] != point[0] 
                and p[1] != point[1]
                and (p[0], point[1]) in self.points 
                and (point[0], p[1]) in self.points):               
                    count1= self.points[(p[0], p[1])]
                    count2=self.points[(p[0], point[1])]
                    count3=self.points[(point[0], p[1])]
                    res += count1 *count2 *count3
        return res
        
