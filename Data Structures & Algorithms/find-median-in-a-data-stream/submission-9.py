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
        if len(self.lower) > len(self.upper):
            return -self.lower[0]

        if len(self.upper) > len(self.lower):
            return self.upper[0]

        return (-self.lower[0] + self.upper[0]) / 2