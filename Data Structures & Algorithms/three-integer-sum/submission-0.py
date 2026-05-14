class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicate i
                continue
            t = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                lr_sum = nums[l] + nums[r]
                if lr_sum == t:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1  # skip duplicate l
                    while l < r and nums[r] == nums[r-1]: r -= 1  # skip duplicate r
                    l += 1
                    r -= 1
                elif lr_sum < t:
                    l += 1
                else:
                    r -= 1
        return res