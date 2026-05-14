from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        nums_counter=nums_counter.most_common(k)
        print(nums_counter)
        return [num for num, count in nums_counter]
