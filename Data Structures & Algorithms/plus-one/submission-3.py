class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(str(d) for d in digits)
        res = int(s)+1
        f = []
        for i in str(res):
            f.append(int(i))
        return f