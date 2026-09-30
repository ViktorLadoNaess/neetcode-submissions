class Solution:
    def isHappy(self, n: int) -> bool:
        
        def nxt(n):
            return sum(int(d)**2 for d in str(n))
        slow = n
        fast= nxt(n)
        while fast != 1 and slow != fast:
            slow= nxt(slow)
            fast=nxt(nxt(fast))
        return fast==1