class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(c):
            if c ==n:
          
                return 1
            if c>n:
                return 0
            if c in memo:
                return memo[c]
            tmp =dfs(c+1)+dfs(c+2)
            memo[c]=tmp
            return tmp
        dfs(0)
        return memo[0]


