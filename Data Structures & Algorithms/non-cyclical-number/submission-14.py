class Solution:
    def isHappy(self, n: int) -> bool:
        def hap(n):
            return sum([int(d)**2 for d in str(n)])
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = hap(n)
        return  False
