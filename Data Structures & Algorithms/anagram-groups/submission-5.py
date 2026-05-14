from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sigs = defaultdict(list)
        for word in strs:
            sig = tuple(sorted(Counter(word).items()))
            sigs[sig].append(word)
            
        return list(sigs.values())