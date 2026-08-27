from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dp = deque()
        res =[]
        
        r = 0
        while r < len(nums):
            while dp and nums[dp[-1]]<nums[r]:
                dp.pop()
            dp.append(r)

            if dp[0]<=r-k:
                dp.popleft()
            if r >= k - 1:
                res.append(nums[dp[0]])
            r+=1
        return res
        
                
            