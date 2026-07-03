import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        while len(nums) >k:
            heapq.heappop(nums)
        self.h = nums


    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        while len(self.h) >self.k:
            heapq.heappop(self.h)
        return self.h[0]
