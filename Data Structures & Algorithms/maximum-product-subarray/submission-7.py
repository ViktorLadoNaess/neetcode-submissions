class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin =nums[0]
        cmax= nums[0]
        biggest = nums[0]
        for n in nums[1:]:
            oldmin=cmin
            oldmax =cmax

            cmin = min(n, oldmin*n, oldmax*n)
            cmax = max(n, oldmin*n, oldmax*n)
            biggest= max(cmax,biggest)
        return biggest
