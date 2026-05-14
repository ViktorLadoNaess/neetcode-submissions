class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums)
        print(nums)
        left = 0
        max_count = 0
        i=1
        while i in range(len(nums)):
            
            if nums[i] - nums[i-1] !=1:
                print()
                max_count= max(max_count,i-left)
                left = i
            i +=1
        print(i-left)
        return min(max(max_count, i-left), len(nums))