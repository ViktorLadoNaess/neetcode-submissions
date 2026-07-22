class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res=0
        memo ={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            nonlocal res
            if j >= len(t):
                return 1 
            if i >= len(s):
                return 0

            m = dfs(i+1,j)
            if s[i] == t[j]:
                m += dfs(i+1,j+1)
            memo[(i,j)]=m
            
            return m
        
        return dfs(0,0)
            
         

             