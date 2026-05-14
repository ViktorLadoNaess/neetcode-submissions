import heapq

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper =[]
        heapq.heapify(self.lower)
        heapq.heapify(self.upper)

    def addNum(self, num: int) -> None:
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        if len(self.lower)> len(self.upper)+1:
            tmp=heapq.heappop(self.lower)
            heapq.heappush(self.upper, -tmp)
        elif len(self.upper)> len(self.lower)+1:
            tmp=heapq.heappop(self.upper)
            heapq.heappush(self.lower, -tmp)

    def findMedian(self) -> float:
        n= len(self.lower)+ len(self.upper)
        if n %2 == 1:
            ind = (n//2) +1
            if len(self.lower)==ind:
                return -self.lower[0]
            else:
                return self.upper[0]
        if n %2 == 0:
            x = -self.lower[0]
            y = self.upper[0]
            return (x+y)/2