class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(a):
            if a == 0:
                return 0

            if a < 0:
                return float("inf")

            if a in memo:
                return memo[a]

            best = float("inf")

            for coin in coins:
                best = min(best, 1 + dfs(a - coin))

            memo[a] = best
            return best

        ans = dfs(amount)

        return ans if ans != float("inf") else -1