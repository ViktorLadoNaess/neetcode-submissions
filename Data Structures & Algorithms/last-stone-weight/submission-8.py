import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*s for s in stones]
        print(stones)
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            z=x-y
            if z !=0:
                heapq.heappush(stones,z)
        if len(stones)>0:
            return abs(stones[0]) 
        else:
            return 0
