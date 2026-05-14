from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        nums_count =counts.most_common(k)
        return [num for num, vals in nums_count]