class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = 0
        r2= 0
        for n in nums:
            curr = max(r2, r1+n)
            r1= r2
            r2=curr
        return r2
            