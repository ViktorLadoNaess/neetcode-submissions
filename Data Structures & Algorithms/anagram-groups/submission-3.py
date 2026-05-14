from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            sig[key].append(s)

        return list(sig.values())