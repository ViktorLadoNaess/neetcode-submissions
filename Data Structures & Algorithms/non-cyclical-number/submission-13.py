class Solution:
    def isHappy(self, n: int) -> bool:
        if n ==1:
            return True
        def nxt(n):
            return sum([int(d)**2 for d in str(n)])
        slow =n
        fast = nxt(n)
        while slow != fast:
            slow = nxt(slow)
            fast = nxt(nxt(fast))
            if fast == 1 or slow ==1:
                return True
        return False


