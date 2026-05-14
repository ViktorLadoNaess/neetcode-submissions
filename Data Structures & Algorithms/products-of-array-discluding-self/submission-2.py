class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_of_all_non_zero = 1
        for num in nums:
            if num == 0:
                zero_count +=1
            else:
                product_of_all_non_zero *=num
        result = []
        if zero_count >1:
            return [0]*len(nums)

        if zero_count ==1:
            for i in nums:
                if i !=0:
                    result.append(0)
                else: 
                    result.append(int(product_of_all_non_zero))
            return result
                
        for i in nums:
                result.append(int(product_of_all_non_zero/i))
        return result
