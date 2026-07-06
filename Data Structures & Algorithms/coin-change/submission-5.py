class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(val):
            if val <0:
                return float('inf')
            if val == 0:
                return 0
            if val in memo:
                return memo[val]
            m = float('inf')
            for c in coins:
                m = min(m,dfs(val-c)+1)
            memo[val]= m

            return m
        return -1 if dfs(amount)== float('inf') else dfs(amount)