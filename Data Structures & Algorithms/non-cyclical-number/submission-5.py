class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n_str = str(n)
            res = 0
            for i in n_str:
                dig = int(i)
                res += pow(dig,2)
            n = res
        return False

