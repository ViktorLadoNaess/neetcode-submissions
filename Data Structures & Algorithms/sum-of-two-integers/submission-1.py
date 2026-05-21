class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF      # keeps only 32 bits
        max_int = 0x7FFFFFFF   # largest positive 32-bit int

        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        # convert from unsigned 32-bit to signed integer
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)