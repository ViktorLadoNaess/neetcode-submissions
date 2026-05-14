class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_of_non_zero = 1
        zero_count =0
        for i in nums:
            if i == 0:
                zero_count +=1
            else:
                product_of_non_zero *= i
        
        if zero_count > 1:
            return [0]*len(nums)
        result =[]
        for i in nums:
            if i !=0 and zero_count== 0 :
                result.append(int(product_of_non_zero/i))
            elif i !=0 and zero_count== 1 :
                result.append(0)
            else:
                result.append(int(product_of_non_zero))
        return result
