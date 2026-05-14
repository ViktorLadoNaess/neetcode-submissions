from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_d = Counter(nums)
        print(nums_d)
        print(nums_d.items())

        
        return [val for val, count in  nums_d.most_common(k) ]