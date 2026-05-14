class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(k,len(nums)+1):
            window = nums[i-k:i]

            res.append(max(window))
        return res