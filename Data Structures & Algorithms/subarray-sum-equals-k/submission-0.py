class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = 0
        res = 0

        count = {0: 1}

        for i in nums:
            prefix += i
            if prefix - k in count:
                res += count[prefix - k]

            count[prefix] = count.get(prefix, 0) + 1

        return res