import heapq

class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        heap = self.heap.copy()
        n = len(heap)

        if n % 2 == 1:
            # pop until we reach the middle element
            for _ in range(n // 2):
                heapq.heappop(heap)

            return heapq.heappop(heap)

        else:
            # pop until we reach the first middle element
            for _ in range(n // 2 - 1):
                heapq.heappop(heap)

            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            return (x + y) / 2