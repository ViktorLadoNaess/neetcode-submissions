class Solution:
    def rob(self, nums: List[int]) -> int:
        n_1 = 0
        n_2 = 0
        for h in nums:
            curr = max(n_2+h,n_1)
            n_2 = n_1
            n_1= curr
        return curr