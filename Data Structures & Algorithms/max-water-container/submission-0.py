class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mvol = 0
        l = 0
        r = len(heights)-1
        while l<r:
            vol = min(heights[l],heights[r]) * (r-l)
            print(f'heights[l]:{heights[l]},heights[r]:{heights[r]}) * r: {r}, l:{l} vol:{vol} ')
           
            mvol = max(vol,mvol)
            
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return mvol

        
