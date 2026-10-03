class Solution:
    def climbStairs(self, n: int) -> int:
        n_2 , n_1 =1,1
        c= 0 
    
        for _ in range(2,n+1):
            tmp= n_1+n_2
            n_2= n_1
            n_1 = tmp
        return n_1