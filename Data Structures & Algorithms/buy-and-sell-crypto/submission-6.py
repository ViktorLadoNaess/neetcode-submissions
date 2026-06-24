class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        m = prices[0]
        for i in prices[1:]:
            res = max(res, i-m)
            m = min(i, m)
        return res