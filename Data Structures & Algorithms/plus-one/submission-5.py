class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''.join(str(s) for s in digits)
        res = int(res)+1
        r =[]
        for i in str(res):
            r.append(i)
        return r