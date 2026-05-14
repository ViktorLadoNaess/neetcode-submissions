from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = Counter(s1)
        n1, n2 = len(s1), len(s2)

        for l in range(n2 - n1 + 1):
            tmp = letters.copy()
            r = l
            # consume as long as the next char is still needed
            while r < n2 and tmp[s2[r]] > 0:
                tmp[s2[r]] -= 1
                r += 1
            # if we consumed exactly all of s1’s letters, it’s a match
            if all(v == 0 for v in tmp.values()):
                return True

        return False
