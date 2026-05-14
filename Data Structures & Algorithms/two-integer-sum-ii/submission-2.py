class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        while left <len(numbers)-1:
            t = target-numbers[left]
            for right in range(left, len(numbers)):
                if numbers[right] == t:
                    return [left+1, right+1]
            left +=1
        
                