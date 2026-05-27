class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo ={}
        def dfs(r,c): 
            if r == m-1 and c ==n-1:
                return 1
            if (r>m-1 or c > n-1):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            else: 
                memo[(r,c)]= dfs(r+1,c)+dfs(r,c+1)
            return dfs(r+1,c)+dfs(r,c+1)
        return dfs(0,0)
            
            