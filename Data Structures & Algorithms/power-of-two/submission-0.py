class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = n
        while True:
            if res == 1: break
            if res <2: return False
            
            res = res/2
        return True
        