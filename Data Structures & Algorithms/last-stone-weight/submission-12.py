import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while stones and len(stones)> 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            res = x-y 
            if res != 0:
                heapq.heappush(stones,res)
        if stones:
            return abs(stones[0])
        else:
            return 0

            