class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        res = 0
        for i in prices:
            res = max(res,i-m)
            m = min(i,m)
        
        return res