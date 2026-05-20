class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(word):
            if len(word) == 0:
                return True

            if word in memo:
                return memo[word]

            for w in wordDict:
                if word.startswith(w):
                    l = len(w)
                    res = dfs(word[l:])

                    if res == True:
                        memo[word] = True
                        return True

            memo[word] = False
            return False

        return dfs(s)