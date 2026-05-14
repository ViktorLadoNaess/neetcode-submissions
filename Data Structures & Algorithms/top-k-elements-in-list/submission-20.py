from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_cnt = Counter(nums)
        return [num for num, _ in nums_cnt.most_common(k)]