class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        n_1=2
        n_2=1

        for n in range(3, n+1):
            curr = n_1+ n_2
            n_2=n_1
            n_1 = curr
        
        return n_1