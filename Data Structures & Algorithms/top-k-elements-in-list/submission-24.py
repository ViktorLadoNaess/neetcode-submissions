from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        print(num_counts.most_common(k))
        return [num for num, val in num_counts.most_common(k)]