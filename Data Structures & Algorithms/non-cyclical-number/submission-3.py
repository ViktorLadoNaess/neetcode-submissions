class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while True:
            n = sum(int(d)**2 for d in str(n))
            print(n)
            if n ==1:
                return True
            if n in seen:
                return False
            seen.add(n)
        

