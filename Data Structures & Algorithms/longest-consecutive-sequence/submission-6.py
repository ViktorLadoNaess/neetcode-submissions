class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums)
        max_consec = 0
        left = 0
        i = 1
        print(nums)
        while i <len(nums):
            if nums[i]-nums[i-1]!=1:
                max_consec =max(max_consec, i-left)
                left = i
            print(max_consec)
            i+=1

        return min(max(max_consec, i-left), len(nums))

