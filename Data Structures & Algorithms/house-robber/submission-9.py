class Solution:
    def rob(self, nums: List[int]) -> int:
        n_2=0
        n_1 = 0

        for num in nums: 
            curr = max(n_1, n_2+num)
            n_2= n_1
            n_1 = curr
        return curr
            