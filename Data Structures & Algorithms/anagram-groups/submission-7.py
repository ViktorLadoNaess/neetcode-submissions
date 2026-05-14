from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sigs = defaultdict(list)
        for word in strs:
            sig = Counter(word)
            sig = tuple(sorted(sig.items()))
            sigs[sig].append(word)
        print(sigs.values())
        return list(sigs.values())