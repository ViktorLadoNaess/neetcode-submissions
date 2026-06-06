from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_c = Counter(nums).most_common(k)
        return [num for num, count in num_c]