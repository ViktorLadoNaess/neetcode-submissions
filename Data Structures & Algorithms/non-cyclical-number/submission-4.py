class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n not in seen:
            if n ==1:
                return True
            seen.add(n)
            n_s= str(n)
            res = 0
            for i in range(len(n_s)):
                res += pow(int(n_s[i]), 2)
            n = res
        return False