from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res =[]
        r=0
        while r<len(nums):
            #print(f'dq at start:{dq}')
            while dq and nums[dq[-1]]<=nums[r]:
                dq.pop()
            dq.append(r)
            #print(f'dq at post max filter:{dq}')
            while dq[0]<=r-k:
                dq.popleft()
            if r >=k-1:
                res.append(nums[dq[0]])
            r+=1
            #print(f'res at post max filter:{res}')
        return res
