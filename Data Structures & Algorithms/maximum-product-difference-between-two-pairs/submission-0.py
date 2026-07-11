class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums.pop()*nums.pop())- (nums[0]*nums[1])