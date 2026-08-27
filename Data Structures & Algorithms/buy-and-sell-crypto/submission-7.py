class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        mp= 0
        for r in prices[1:]:
            print(mp)
            mp = max(mp,r-mi)
            mi = min(r,mi)
        return mp