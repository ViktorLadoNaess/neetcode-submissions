class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_min = nums[0]
        c_max = nums[0]
        biggest = nums[0]

        for n in nums[1:]:
            old_max = c_max
            old_min = c_min

            c_max = max(n, n * old_max, n * old_min)
            c_min = min(n, n * old_max, n * old_min)

            biggest = max(biggest, c_max)
        return biggest