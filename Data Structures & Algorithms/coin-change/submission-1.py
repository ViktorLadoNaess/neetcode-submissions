class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(target):
            if target == 0:
                return 0

            if target < 0:
                return float("inf")

            if target in memo:
                return memo[target]

            best = float("inf")

            for coin in coins:
                best = min(best, 1 + dfs(target - coin))

            memo[target] = best
            return best

        ans = dfs(amount)

        return ans if ans != float("inf") else -1