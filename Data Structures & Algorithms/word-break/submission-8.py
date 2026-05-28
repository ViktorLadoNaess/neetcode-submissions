class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(remaining):
            if len(remaining) == 0:
                return True

            if remaining in memo:
                return memo[remaining]

            for w in wordDict:
                if remaining.startswith(w):
                    l = len(w)

                    if dfs(remaining[l:]):
                        memo[remaining] = True
                        return True

            memo[remaining] = False
            return False

        return dfs(s)