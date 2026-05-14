from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        l=0
        r = len(t)
        indexes = [0,0]
        m = len(s)+1
        print(Counter(s[:r]))
        if target == Counter(s[:r]):
            print(target)
            return s[0:r]
        while r == len(s) or r <= len(s):
            if target <= Counter(s[l:r]):
                if r -l  <m:
                    print(f"m:{m} r:{r}, l:{l}")
                    indexes=[l,r]
                    m = r-l
                l+=1
            else:
                r +=1

        if m == len(s)+1:
            return ""
        return s[indexes[0]:indexes[1]]