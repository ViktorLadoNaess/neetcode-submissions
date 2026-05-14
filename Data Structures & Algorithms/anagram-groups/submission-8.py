from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sigs= defaultdict(list)
        for s in strs:
            sig = (tuple(sorted(Counter(s).items())))
            sigs[sig].append(s)
        return[w for s, w in sigs.items()]