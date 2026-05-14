import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x == y:
                continue
            else:
                print(f'y{y}, x{x}, y-x: {y-x}')
                heapq.heappush(heap, y-x)
        if len(heap)>0:
            return abs(heap[0])
        else: 
            return 0