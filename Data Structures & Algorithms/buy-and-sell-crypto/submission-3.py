class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p= 0
        m = prices[0]
        for i in prices[1:]:
            p = max(p,i - m)
            m = min(m,i)
        return p

