class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(c) for c in digits)
        print(s)
        res = 1 + int(s)
        f = []
        for v in str(res):
            f.append(v)
        return f