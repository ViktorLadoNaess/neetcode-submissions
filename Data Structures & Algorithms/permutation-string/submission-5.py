from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        target = Counter(s1)
        window = Counter(s2[:n])

        if window == target:
            return True
        for i in range(1,len(s2)): 
            if n+i>len(s2):
                break
            window = Counter(s2[i:n+i])
            if window == target:
                return True
        return False
            