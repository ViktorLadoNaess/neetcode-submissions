class Solution:
    def rob(self, nums: List[int]) -> int:
        n_1 = 0
        n_2= 0
        for i in nums:
            curr = max(n_1,n_2+i)
            n_2=n_1
            n_1=curr
        return curr