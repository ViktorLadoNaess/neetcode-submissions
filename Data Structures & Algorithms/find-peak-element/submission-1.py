class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                # We are descending, so a peak exists at mid or to its left.
                r = mid
            else:
                # We are ascending, so a peak exists to the right.
                l = mid + 1

        return l