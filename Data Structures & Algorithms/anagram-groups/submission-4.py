from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sigs = defaultdict(list)
        for w in strs:
            sig=tuple(sorted(Counter(w).items()))
            print(sig)
            sigs[sig].append(w)
        return list(sigs.values())
