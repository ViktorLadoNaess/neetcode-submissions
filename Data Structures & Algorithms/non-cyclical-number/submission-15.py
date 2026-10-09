class Solution:
    def isHappy(self, n: int) -> bool:
        def hap(n):
            return sum([int(d)**2 for d in str(n)])
        slow = n
        fast = hap(n)
        while slow !=1 and fast != slow:
            slow = hap(slow)
            fast = hap(hap(fast))
        return fast ==1 
