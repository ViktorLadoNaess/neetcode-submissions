class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(val):
            if val == 0:
                return 0
            if val < 0:
                return float('inf')
            if val in memo:
                return memo[val]
            res = float('inf')
            for i in coins:
                res = min(res, dfs(val-i)+1)
            memo[val] = res
            return res
        return dfs(amount) if dfs(amount)!= float('inf') else -1