class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count=0
        prod_non_0=1
        for i in nums:
            if i ==0:
                zero_count +=1
            else: 
                prod_non_0 *= i
        
        if zero_count >=2:
            return [0]*(len(nums))
        result =[]
        if zero_count == 1:
            for i in nums:
                if i !=0:
                    result.append(0)
                else: 
                    result.append(prod_non_0)
            return result
        for i in nums:
            result.append(int(prod_non_0/i))
        return result

