from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig = defaultdict(list)
        for i in range(len(strs)):
            key = tuple(sorted(Counter(strs[i]).items()))
            sig[key].append(strs[i])
        print(sig.values())
        return list(sig.values())

