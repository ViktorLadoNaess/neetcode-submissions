class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c.lower() for c in s if c.isalnum())
        print(clean)
        print(clean[::-1])
        return clean==clean[::-1]