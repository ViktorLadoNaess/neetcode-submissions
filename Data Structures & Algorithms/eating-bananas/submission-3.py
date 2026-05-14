class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, math.ceil(max(piles) / (h // len(piles)))
        while l <= r:
            k = (l + r) // 2
            hrs = sum(math.ceil(pile / k) for pile in piles)
            if hrs <= h:
                r = k - 1
            else:
                l = k + 1
        return l