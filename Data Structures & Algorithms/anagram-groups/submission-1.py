from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            d = defaultdict(list)
            for word in strs:
                signature = ''.join(sorted(word))
                d[signature].append(word)
            return list(d.values())
