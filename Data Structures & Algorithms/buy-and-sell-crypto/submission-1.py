class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_c = prices[0]
        p =0
        for i in prices[1:]:
            min_c = min(min_c,i)
            p = max(i-min_c,p)
            

        return max(0, p)
        


            

        
        