class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        msf= prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-msf)
            msf = min(msf,prices[i] )

        return profit