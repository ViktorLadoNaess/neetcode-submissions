class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_min = nums[0]
        c_max = nums[0]
        biggest = nums[0]

        for i in nums[1:]:
            old_min = c_min
            old_max = c_max

            c_min = min(i,old_min*i,old_max*i)
            c_max = max(i,old_min*i,old_max*i)
            biggest = max(biggest,c_max,c_min)
        return biggest


            
