class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1, s[l + 1:r]

        m = 0
        p = ""

        for i in range(len(s)):
            tmpm, pal = expand(i, i)       # odd length
            if tmpm > m:
                m = tmpm
                p = pal

            tmpm, pal = expand(i, i + 1)   # even length
            if tmpm > m:
                m = tmpm
                p = pal

        return p