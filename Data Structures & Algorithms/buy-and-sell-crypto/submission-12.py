class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        m = 0
        while r <len(prices):
            if prices[r]<prices[l]:
                l =r
            else:
                m = max(m, prices[r]-prices[l])
                r+=1
        return m