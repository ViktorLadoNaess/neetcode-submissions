import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        table = str.maketrans('', '', string.punctuation)
        clean = s.translate(table).lower()
        clean =clean.replace(" ", "")
        return clean ==clean[::-1]