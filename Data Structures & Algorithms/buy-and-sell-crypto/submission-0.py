class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l, r = 0,1

        while r<len(prices):
            if prices[l]<prices[r]:
                prof= -prices[l]+prices[r]
                maxProf=max(maxProf,prof)
            else: 
                l =r
            r+=1
        return maxProf

            

        
        