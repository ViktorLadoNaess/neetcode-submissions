class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)
        print(nums)
        i =1 
        left = 0
        max_so_far=0
        while i in range(len(nums)):
            if nums[i]-nums[i-1]!=1:
                max_so_far = max(max_so_far,abs(i-left))
                left=i

            i +=1
        return max(max_so_far, len(nums) - left)  # capture last run

