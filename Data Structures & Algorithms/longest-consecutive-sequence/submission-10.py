class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        mlen= 0
        l = 0
        i = 1
        while i<len(nums):
            if nums[i]- nums[i-1] != 1:
                print(mlen)
                mlen= max(mlen, i-l)
                l = i
            i +=1

        return min(max(mlen, i-l), len(nums))
        