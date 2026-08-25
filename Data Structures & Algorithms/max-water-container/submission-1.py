class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m= 0
        l =0
        r = len(heights)-1
        while l <r:
            m = max(m, (r-l)*min(heights[r],heights[l]))
            if heights[l]>heights[r]:
                r -=1
            else:
                l+=1
        return m
