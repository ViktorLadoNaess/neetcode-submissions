class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid = r'[^a-z0-9]'
        s = re.sub(valid,'', s)
        return s== s[::-1]