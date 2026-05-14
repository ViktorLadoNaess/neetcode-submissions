import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        table = str.maketrans('', '', string.punctuation)
        clean = s.translate(table).lower()
        clean =clean.replace(" ", "")
        #return clean ==clean[::-1] time O(1), space = O(n)
        l, r = 0, len(clean)-1
        while l < r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True