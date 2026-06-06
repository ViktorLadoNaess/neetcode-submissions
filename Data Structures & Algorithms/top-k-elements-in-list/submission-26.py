from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums).most_common(k)
        print(n)
        return [num for num, count in n]